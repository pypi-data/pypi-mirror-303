import os, time, json
from urllib.parse import *
import threading
from datetime import datetime, timedelta
import calendar
from threading import Thread, current_thread, Lock
import math
import psutil
import websocket
import uuid
import queue
import subprocess, platform
from mecord import store
from mecord import xy_pb
from mecord import task
from mecord import constant 
from mecord import utils
from mecord import taskUtils
import mecord.pb.tarsproxy_pb2 as tarsproxy_pb2
from logging.handlers import RotatingFileHandler
import logging

thisFileDir = os.path.dirname(os.path.abspath(__file__))
waitlastTask = os.path.join(thisFileDir, f"waitlastTask")
stop_thread_file = os.path.join(thisFileDir, "stop.thread")
refreshMessage = os.path.join(thisFileDir, "refreshMessage")
refresh_map = {'test': True, 'sg': True, 'usdc': True}
gettask_flag = {'test': True, 'sg': True, 'usdc': True}
test_no_request = 0
logFilePath = f"{os.path.dirname(os.path.abspath(__file__))}/ConnectThread.log"
file_handler = RotatingFileHandler(logFilePath, maxBytes=1024*1024*20, backupCount=5)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter(fmt='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
logger = logging.getLogger('MecordConnectThread')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
def can_use_longconnect():
    def getCommandResult(cmd):
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            if result.returncode == 0:
                return result.stdout.decode(encoding="utf8", errors="ignore").replace("\n","").strip()
        except subprocess.CalledProcessError as e:
            print(f"getCommandResult fail {e}")
        return ""
    if platform.system() == 'Windows':
        return True
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        return len(getCommandResult("which at")) > 0 and len(getCommandResult("which atd")) > 0

class MecordTaskExecutorThread(Thread):
    THEADING_LIST = []
    max_counter = 1
    cur_counter = 0
    is_running = False
    task_queue = None
    ttt = 0
    
    def appendTask(self, data, timeout, country, callback, gettask, map, ext=""):
        addQueue_time = int(time.time()*1000)
        self.cur_counter+=1
        self.task_queue.put([data, timeout, country, callback, gettask, map, ext])
        name = str(current_thread().name)
        if self.mtype:
            if name[-2:] == '-h':
                self.high_cur_counter += 1
            else:
                self.low_cur_counter += 1
        try:
            taskUUID = data["taskUUID"]
            # taskUtils.taskPrint(taskUUID, f"{name} === addQueue {country} task : {taskUUID} time_stamp : {addQueue_time}")
            logger.info(f'{self.name} === addQueue {country} task : {taskUUID} -t {addQueue_time}')
        except Exception as e:
            print(f'data error: {e}')
            
    def idlePower(self, ext=''):
        if self.mtype:
            if ext == '-h':
                return (self.high_max_counter - self.high_cur_counter) if self.high_cur_counter >= 0 else 0
            else:
                return (self.low_max_counter - self.low_cur_counter) if self.low_cur_counter >= 0 else 0
        else:
            return (self.max_counter - self.cur_counter) if self.low_cur_counter >= 0 else 0
    
    def isWorking(self):
        return self.cur_counter > 0

    def __init__(self, mtype='', high_threadNum=1, low_threadNum=1):
        threading.Thread.__init__(self)
        self.mtype = mtype
        self.name = f"MecordTaskExecutorThread"
        self.task_queue = queue.Queue()
        self.max_counter = store.get_multithread()
        self.high_cur_counter = 0
        self.low_cur_counter = 0
        if self.mtype:
            self.high_max_counter = high_threadNum
            self.low_max_counter = low_threadNum
        else:
            self.high_max_counter = 1
            self.low_max_counter = self.max_counter
        self.is_running = True
        self.THEADING_LIST = []
        self.start()

    def taskRunning(self):
        while self.is_running or not self.task_queue.empty():
            try:
                data, timeout, country, callback, gettask, map, ext = self.task_queue.get()
                if data is None: 
                    break
                taskUUID = data["taskUUID"]
                is_counter = False
                is_ok = True
                start_time = calendar.timegm(time.gmtime())
                try:
                    widget_name = json.loads(data['config'])['name']
                except:
                    widget_name = ''
                try:
                    taskUtils.taskPrint(taskUUID, f"{current_thread().name} === receive {country} task : {taskUUID}")
                    # _appendTask(taskUUID, country, name)
                    is_ok, msg, result, is_counter, is_warnning = task.runTask(data, timeout, country, widget_name, _appendTask, gettask, ext, self.next_task, map)
                    if (is_ok == False) and is_warnning:
                        taskUtils.notifyTaskFail(taskUUID, country, msg)
                    callback(taskUUID, is_ok, msg, result)
                    _removeTask(taskUUID)
                except Exception as e:
                    taskUtils.taskPrint(taskUUID, f"{current_thread().name} === {country} task exception : {e}")
                    taskUtils.notifyScriptError(taskUUID, country)
                finally:
                    taskUtils.taskPrint(taskUUID, None)
                if not is_counter:
                    self.next_task(gettask, ext, country)
                taskUtils.saveCounter(taskUUID, country, (calendar.timegm(time.gmtime()) - start_time), is_ok)
                self.task_queue.task_done()

            except Exception as ex:
                taskUtils.taskPrint(None, f"{current_thread().name} === exception : {ex}")
                pass
        lock.acquire()
        if os.path.exists(waitlastTask):
            os.remove(waitlastTask)
        lock.release()
        print(f"   {current_thread().name} taskRunning stop")

    def run(self):
        idx = 1
        for _ in range(0, self.max_counter):
            self.THEADING_LIST.append(Thread(name=f"exector-{idx}",target=self.taskRunning))
            idx+=1
        for t in self.THEADING_LIST:
            t.start()
        while self.is_running:
            time.sleep(5)
        for t in self.THEADING_LIST:
            t.join()
        print(f"   {self.name} stop!")

    def markStop(self):
        self.is_running = False
        print(f"   {self.name} waiting stop")
        for _ in range(self.max_counter*2):
            self.task_queue.put([None, -1, None, None, None, None, None])
        print(f"   {self.name} stop")

    def next_task(self, gettask, ext, country):
        if ext == '-h':
            self.high_cur_counter -= 1
        elif ext == '-l':
            self.low_cur_counter -= 1
        else:
            self.cur_counter -= 1
        # gettask()
        gettask_flag[country] = True


class MecordLongConnectThread(Thread):
    
    def get_url(self):
        return {
            "test": "wss://mecord-beta.2tianxin.com/proxymsg/ws",
            "usdc": "wss://api-us-dc.mecordai.com/proxymsg/ws",
            "us": "wss://api.mecordai.com/proxymsg/ws",
            "sg": "wss://api-inner.mecordai.com/proxymsg/ws" if 'autodl' in utils.get_hostname() else "wss://api-sg-gl.mecordai.com/proxymsg/ws",
        }[self.service_country]
    ws = None
    extend_config = {}
    token = ""
    device_id = ""
    service_country = "test"
    THEADING_LIST = []
    is_running = False
    last_get_task_begin = 0
    last_get_task_end = 0
    reconnect_cnt = 0
    executor: MecordTaskExecutorThread = None
    
    def taskCallback(self, taskUUID, is_ok, msg, result):
        self.TaskNotify(taskUUID, is_ok, msg, result)
        
    def receive_unknow_func(self, body):
        pass
    def receive_GetTask(self, body):
        self.last_get_task_end = calendar.timegm(time.gmtime())
        rsp = xy_pb.aigc_ext_pb2.GetTaskRes()
        rsp.ParseFromString(body)
        get_task_time = int(time.time()*1000)
        if len(rsp.list) > 0:
            print(f"{current_thread().name}=== get data packet, has {len(rsp.list)} task -t {get_task_time}")
            task_list = []
            reply_list = []
            reject_list = []
            for it in rsp.list:
                task_list.append(it.taskUUID)
                if self.executor.idlePower() == 0:  # 为零则不再加入队列
                    reject_list.append(it.taskUUID)
                    continue
                self.executor.appendTask({
                    "taskUUID": it.taskUUID,
                    "pending_count": rsp.count - rsp.limit,
                    "config": it.config,
                    "data": it.data,
                }, rsp.timeout, self.service_country, self.taskCallback, self.GetTask, self.map, self.mtype)
                reply_list.append(it.taskUUID)
            if len(task_list) > 0:
                logger.info(f'{self.name} === get {len(rsp.list)} task, tasklist: {task_list} -t {get_task_time}')
            if len(reply_list) > 0:
                self.TaskReply(reply_list)
                logger.info(f"{self.name} === TaskReply: {str(reply_list)}")
            if len(reject_list) > 0:
                logger.info(f"{self.name} *** TaskReject: {str(reject_list)}")
                # self.TaskReject(reject_list)

    def receive_TaskNotify(self, body):
        rsp = xy_pb.aigc_ext_pb2.TaskNotifyRes()
        rsp.ParseFromString(body)
        timestampe = int(time.time()*1000)
        if rsp.ok and len(rsp.notify_id) > 0:
            xy_pb.resetLastTaskNotify(rsp.task_uuid)
            taskUtils.taskPrint(rsp.task_uuid, f"{current_thread().name}=== task : {rsp.task_uuid} notify server success, timestampe: {timestampe}")
        else:
            taskUtils.taskPrint(rsp.task_uuid, f"{current_thread().name}=== task : {rsp.task_uuid} server fail~~ rsp={rsp}")
        taskUtils.taskPrint(rsp.task_uuid, None)
        logger.info(f'{self.name} === task {rsp.task_uuid} notify={rsp.ok} -t {timestampe}')

    def receive_TaskInfo(self, body):
        rsp = xy_pb.aigc_ext_pb2.TaskInfoRes()
        rsp.ParseFromString(body)

    def on_message(self, ws, message):
        try:
            msg = tarsproxy_pb2.Message()
            msg.ParseFromString(message)
            cases = {
                "mecord.aigc.AigcExtObj_GetTask": self.receive_GetTask,
                "mecord.aigc.AigcExtObj_TaskNotify": self.receive_TaskNotify,
                "mecord.aigc.AigcExtObj_TaskInfo": self.receive_TaskInfo,
            }
            return cases.get(f"{msg.obj}_{msg.func}", self.receive_unknow_func)(msg.body)
        except Exception as ex:
            # print(f'on_message() === error: {ex}')
            pass
    def on_error(self, ws, error):
        logger.info(f'{self.name} === Connection on_error (error: {error})')
        print(f"Connection on_error (error: {error})")
        if 'Handshake status 400 Bad Request' in str(error) and self.reconnect_cnt >= 20:
            self.is_accelerate = False
        if "Connection to remote host was lost" in str(error):
            print(f"close socket & sleep(2)")
            self.socket_close()
            time.sleep(2)
        if self.is_running:
            self.reconnect()
        pass
    def on_close(self, ws, status_code, close_msg):
        print(f"Connection closed (status code: {status_code}, message: {close_msg})")
        time.sleep(1)
        if self.is_running:
            self.reconnect()
    def on_ping(self, ws, message):
        print(f"on_ping... {message}")
    def on_pong(self, ws, message):
        print(f"on_pong... {message}")

    def on_open(self, ws):
        self.GetTask()
        self.reconnect_cnt=0

    def __init__(self, country, executor, mtype=''):
        threading.Thread.__init__(self)
        self.mtype = mtype
        self.name = f"MecordLongConnectThread-{country}{self.mtype}"
        extInfo = {}
        host_name = utils.get_hostname() + ('(H)' if self.mtype == '-h' else '')
        extInfo["host_name"] = host_name
        extInfo["version"] = constant.app_version
        extInfo["device_id"] = utils.generate_unique_id(self.mtype if self.mtype == '-h' else '')
        self.extend_config = extInfo
        self.token = xy_pb.real_token(country)
        self.service_country = country
        self.executor = executor
        self.is_running = True
        self.THEADING_LIST = []
        self.last_get_task_begin = 0
        self.last_get_task_end = 0
        self.reconnect_cnt = 0
        self.latency = ''
        self.is_accelerate = True
        self.socket_init()
        self.map = store.widgetMap()
        self.widgets = self.get_widget()
        self.start()

    def socket_init(self):
        ws_url = self.get_url() if self.is_accelerate else self.get_url().replace('api-inner.mecordai.com', 'api-sg-gl.mecordai.com')
        self.ws = websocket.WebSocketApp(url=ws_url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close,
                                    on_ping=self.on_ping,
                                    on_pong=self.on_pong,
                                    header={
                                        'deviceid':self.extend_config['device_id']
                                    })
        self.ws.on_open = self.on_open

    def socket_start(self):
        if self.ws:
            self.ws.run_forever()
    def reconnect(self):
        logger.info(f'{self.name} === reconnect {self.reconnect_cnt}/60...')
        # print(f"{current_thread().name} === reconnect {self.reconnect_cnt}/60...")
        if self.reconnect_cnt > 60:
            # print(f"{current_thread().name} === 无法连接上服务器，重启")
            # self.is_running = False
            # utils.begin_restart(f"the number of reconnect to {self.service_country} is more than 60 times") #reconnect
            print(f"{current_thread().name} === 无法连接上服务器，重新创建线程")
            remake_file = os.path.join(thisFileDir, f"remake-{self.service_country}")
            with open(remake_file, 'w') as f:
                f.write('')

        else:
            self.reconnect_cnt+=1
            self.socket_close()
            self.socket_init()
    def send_byte(self, b):
        try:
            if self.ws:
                self.ws.send_bytes(b)
        except Exception as e:
            logger.info(f'{self.name} === send_byte() error: {e}')


    def socket_close(self):
        if self.ws:           
            self.ws.close()
        self.ws = None

    def socket_bypass(self):
        last_heart_pts = calendar.timegm(time.gmtime())
        last_check_service_work_status_pts = last_heart_pts
        self.last_get_task_begin = last_heart_pts
        wait_time = 1 if self.service_country == "sg" else 3
        while self.is_running:
            global refresh_map
            if os.path.exists(refreshMessage):
                refresh_map = {'test': True, 'sg': True, 'usdc': True}
                try:
                    os.remove(refreshMessage)
                except:
                    pass
            if refresh_map[self.service_country]:
                time.sleep(2)
                self.map = store.widgetMap()
                self.widgets = self.get_widget()
                self.GetTask()
                refresh_map[self.service_country] = False
            elif gettask_flag[self.service_country]:
                self.GetTask()
                gettask_flag[self.service_country] = False

            cur_pts = calendar.timegm(time.gmtime())
            if cur_pts - last_heart_pts > 10:

                self.send_byte(self._pb_pack("", None))
                # if 3 == random.randint(0, 5):
                print(f"{current_thread().name}-{self.service_country} === heartbeat {self.latency}")

                # if self.service_country != "test":
                    #Previous tasks may have failed due to network problems, so collect and resend
                    # xy_pb.retryLastTaskNotify()
                last_heart_pts = cur_pts
            if cur_pts - last_check_service_work_status_pts > 120 and self.executor.isWorking() == False:
                if abs(self.last_get_task_end - self.last_get_task_begin) > 180:   # 不工作状态且3分钟没拉到任务，重建新线程
                    #from wuyongcong@xinyu668.com ,may be server is disconnect but client dont know
                    print(f"{current_thread().name}-{self.service_country} === 重启")
                    # self.is_running = False
                    # utils.begin_restart(f"did not connect to {self.service_country}") #reconnect
                    remake_file = os.path.join(thisFileDir, f"remake-{self.service_country}")
                    with open(remake_file, 'w') as f:
                        f.write('')
                if cur_pts - self.last_get_task_end > 60:  # 不工作状态且超过1分钟没获取到任务
                    #request once this device status
                    self.GetTask()
                    print(f"{current_thread().name}-{self.service_country} === trigger timeout getTask!")
                last_check_service_work_status_pts = cur_pts
            if cur_pts - self.last_get_task_begin > 10:  # 超过10s没有主动发起拉任务
                self.GetTask()
                last_check_service_work_status_pts = cur_pts
            if self.executor.isWorking() == False and cur_pts - self.last_get_task_begin > 20:
                print(f"{current_thread().name}-{self.service_country} === trigger timeout getTask!")
                self.GetTask()
                last_check_service_work_status_pts = cur_pts
            time.sleep(wait_time)
            xy_pb.retryLastTaskNotify()
        print(f"   {current_thread().name}-{self.service_country} heartbeat stop")
        if os.path.exists(refreshMessage):
            os.remove(refreshMessage)

    def _pb_pack(self, func, req):
        opt = {
            "lang": "zh-Hans",
            "region": "CN",
            "appid": "80",
            "application": "mecord",
            "version": "1.0",
            "X-Token": self.token,
            "uid": "1",
        }
        input_req = xy_pb.rpcinput_pb2.RPCInput(obj="mecord.aigc.AigcExtObj", func=func, req=(req.SerializeToString() if req else None), opt=opt)
        return input_req.SerializeToString()

    def get_widget(self):
        widgets = []
        map = self.map
        if self.mtype == '-h':
            for it in map:
                if isinstance(map[it], (dict)):
                    if map[it]["isBlock"] is False and map[it].get('isGPU', False):
                        widgets.append(it)
        elif self.mtype == '-l':
            for it in map:
                if isinstance(map[it], (dict)):
                    if map[it]["isBlock"] is False and map[it].get('isGPU', False) is False:
                        widgets.append(it)
        else:
            for it in map:
                if isinstance(map[it], (dict)):
                    if map[it]["isBlock"] is False:
                        widgets.append(it)
                else:
                    widgets.append(it)
        return widgets

    def GetTask(self):
        if not os.path.exists(stop_thread_file):
            req = xy_pb.aigc_ext_pb2.GetTaskReq()
            req.limit = self.executor.idlePower(self.mtype)
            # print(f"=============== gettask{self.mtype} {req.limit}")
            if req.limit <= 0:
                return
            req.version = xy_pb.constant.app_version
            req.DeviceKey = self.extend_config["device_id"]
            for widget in self.widgets:
                req.widgets.append(widget)
            if len(req.widgets) == 0:
                return
            req.token = self.token
            # req.extend = self.extend_config
            # self.extend_config["dts"] = datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
            self.extend_config["trace_id"] = ''.join(str(uuid.uuid4()).split('-'))
            req.extend = json.dumps(self.extend_config)
            req.apply = True
            self.last_get_task_begin = calendar.timegm(time.gmtime())
            send_byte_time = int(time.time()*1000)
            self.send_byte(self._pb_pack("GetTask", req))
            logger.info(f'{self.name} === waiting {req.limit} task, widgets: {req.widgets} -t {send_byte_time} trace_id: {self.extend_config["trace_id"]}')
            if self.mtype:
                print(f'{self.name} waiting next {req.limit} task, widgets: {req.widgets} -t {send_byte_time} trace_id: {self.extend_config["trace_id"]}')
            else:
                print(f'{self.name} waiting next {req.limit} task -t {send_byte_time} trace_id: {self.extend_config["trace_id"]}')

    def TaskReply(self, tasklist):
        task_item = xy_pb.aigc_ext_pb2.TaskItem()
        req = xy_pb.aigc_ext_pb2.TaskReplyReq()
        for task in tasklist:
            task_item.taskUUID = task
            req.list.append(task_item)
        self.send_byte(self._pb_pack("TaskReply", req))

    def TaskInfo(self, taskUUID):
        req = xy_pb.aigc_ext_pb2.TaskInfoReq()
        req.taskUUID = taskUUID
        req.findTaskResult = True
        self.send_byte(self._pb_pack("TaskInfo", req))

    def TaskNotify(self, taskUUID, status, msg, dataStr):
        req = xy_pb.aigc_ext_pb2.TaskNotifyReq()
        req.version = constant.app_version
        req.taskUUID = taskUUID
        if status:
            req.taskStatus = xy_pb.common_ext_pb2.TaskStatus.TS_Success
        else:
            req.taskStatus = xy_pb.common_ext_pb2.TaskStatus.TS_Failure
        req.failReason = msg
        req.data = dataStr
        # req.extend = self.extend_config
        self.extend_config["trace_id"] = ''.join(str(uuid.uuid4()).split('-'))
        req.extend = json.dumps(self.extend_config)
        xy_pb.saveTaskNotifyData(self.service_country, taskUUID, status, msg, dataStr)
        taskUtils.taskPrint(taskUUID, f"{current_thread().name}=== notify {self.service_country} task : {taskUUID}")
        self.send_byte(self._pb_pack("TaskNotify", req))

    def TaskReject(self, reject_list):
        for taskUUID in reject_list:
            req = xy_pb.aigc_ext_pb2.TaskNotifyReq()
            req.version = constant.app_version
            req.taskUUID = taskUUID
            req.taskStatus = xy_pb.common_ext_pb2.TaskStatus.TS_Failure
            req.failReason = 'Tasks over limit'
            req.data = ''
            self.extend_config["trace_id"] = ''.join(str(uuid.uuid4()).split('-'))
            req.extend = json.dumps(self.extend_config)
            self.send_byte(self._pb_pack("TaskNotify", req))

    def run(self):
        self.THEADING_LIST.append(Thread(target=self.socket_bypass))
        for t in self.THEADING_LIST:
            t.name += self.mtype
            t.start()
        while self.is_running:
            self.socket_start()
            print(f"   {self.name} socket stop")
            time.sleep(1)

    def markStop(self):
        self.is_running = False
        logger.info(f'{self.name} === markStop')
        print(f"   {self.name} waiting stop")
        for t in self.THEADING_LIST:
            t.join()
        while os.path.exists(waitlastTask):
            time.sleep(1)
        if self.service_country != "test":
            xy_pb.retryLastTaskNotify()
        if self.ws:
            self.ws.close()
            self.ws = None
        print(f"   {self.name} stop")

    def remake(self):
        self.is_running = False
        logger.info(f'{self.name} === remake thread')
        print(f"   {self.name} waiting stop")
        for t in self.THEADING_LIST:
            t.join()
        if self.service_country != "test":
            xy_pb.retryLastTaskNotify()
        if self.ws:
            self.ws.close()
            self.ws = None

lock = Lock()
task_config_file = os.path.join(thisFileDir, f"task_config.txt")
def _readTaskConfig():
    if os.path.exists(task_config_file) == False:
        with open(task_config_file, 'w') as f:
            json.dump({
                "last_task_pts": 0
            }, f)
    with open(task_config_file, 'r') as f:
        data = json.load(f)
    return data
def _saveTaskConfig(data):
    with open(task_config_file, 'w') as f:
        json.dump(data, f)
def _appendTask(taskUUID, country, name, pid):
    lock.acquire()
    task_config = _readTaskConfig()
    task_config[taskUUID] = {
        "country": country,
        "pts": calendar.timegm(time.gmtime()),
        "name": name,
        "pid": pid
    }
    task_config["last_task_pts"] = task_config[taskUUID]["pts"]
    _saveTaskConfig(task_config)
    lock.release() 
def _clearTask():
    lock.acquire()
    task_config = {
        "last_task_pts": 0
    }
    try:
        with open(task_config_file, 'r') as f:
            data = json.load(f)
            for taskUUid in data:
                if taskUUid == 'last_task_pts':
                    continue
                else:
                    xy_pb.taskReject(taskUUid, data[taskUUid]['country'])
    except Exception as e:
        print(f'_clearTask() ERROR: {e}')
    _saveTaskConfig(task_config)
    lock.release()
def _removeTask(taskUUID):
    lock.acquire()
    task_config = _readTaskConfig()
    if taskUUID in task_config:
        del task_config[taskUUID]
    _saveTaskConfig(task_config)
    lock.release() 
def _taskCreateTime(taskUUID):
    pts = 0
    lock.acquire()
    task_config = _readTaskConfig()
    if taskUUID in task_config:
        pts = task_config[taskUUID]["pts"]
    lock.release()
    return pts 
def _getTaskConfig():
    lock.acquire()
    task_config = _readTaskConfig()
    lock.release() 
    return task_config


class MecordShortConnectThread(Thread):
    is_running = False
    service_country = "sg"
    executor: MecordTaskExecutorThread = None

    def __init__(self, country, executor, mtype=''):
        super().__init__()
        self.name = f"MecordShortConnectThread-{country}{mtype}"
        self.is_running = True
        self.ext = None
        self.service_country = country
        self.executor = executor
        self.mtype = mtype
        self.map = store.widgetMap()
        self.widgets = self.get_widget()
        self.start()

    
    def taskCallback(self, taskUUID, is_ok, msg, result):
        start_time = int(time.time()*1000)
        logger.info(f"{self.name} === {taskUUID} task is_ok={is_ok} -t {start_time}")
        notify = xy_pb.TaskNotify(self.service_country, taskUUID, is_ok, msg, result, keep_alive=True, timeout=3)
        if notify is False:
            notify = xy_pb.TaskNotify(self.service_country, taskUUID, is_ok, msg, result, keep_alive=True, timeout=3)
        end_time = int(time.time()*1000)
        logger.info(f"{self.name} === {taskUUID} task notify={notify} -t {end_time} -c {end_time-start_time}ms")

    def run(self):
        print(f"   {self.name} start")
        wait_time = 1 if self.service_country == "sg" else 3
        while self.is_running:
            global refresh_map, test_no_request
            if os.path.exists(refreshMessage):
                refresh_map = {'test': True, 'sg': True, 'usdc': True}
                try:
                    os.remove(refreshMessage)
                except:
                    pass
            if refresh_map[self.service_country]:
                time.sleep(2)
                self.map = store.widgetMap()
                self.widgets = self.get_widget()
                refresh_map[self.service_country] = False
            limit = self.executor.idlePower(self.mtype)
            if limit >= 1 and len(self.widgets) >= 1 and (test_no_request < 5 or self.service_country == 'test'):
                traceid = ''.join(str(uuid.uuid4()).split('-'))
                logger.info(f'{self.name} === wait {limit} tasks, widgets: {self.widgets} -t {int(time.time())} traceid: {traceid}')
                try:
                    datas, timeout = xy_pb.GetTask(self.service_country, self.widgets, limit=limit, keep_alive=True, reqid=traceid, ext=self.ext)
                    if len(datas) > 0:
                        logger.info(f'{self.name} === get {len(datas)} task -t {int(time.time()*1000)} traceid: {traceid}')
                        task_list = []
                        for it in datas:
                            task_list.append(it['taskUUID'])
                            self.executor.appendTask(it, timeout, self.service_country, self.taskCallback, self.next_task, self.map, self.mtype)
                        logger.info(f'{self.name} === GetTaskList {str(task_list)} -t {int(time.time()*1000)} traceid: {traceid}')

                except Exception as ex:
                    logger.info(f"{self.name} === get task exception : {ex}")
                if self.service_country == 'test':
                    test_no_request = 0
            elif self.service_country == 'test':
                test_no_request += 1
            time.sleep(wait_time)
            #Previous tasks may have failed due to network problems, so collect and resend
            xy_pb.retryLastTaskNotify()
        print(f"   {self.name} stop")
        if os.path.exists(refreshMessage):
            os.remove(refreshMessage)
    def next_task(self):
        pass

    def get_widget(self):
        widgets = []
        map = self.map
        if self.mtype == '-h':
            for it in map:
                if isinstance(map[it], (dict)):
                    if map[it]["isBlock"] is False and map[it].get('isGPU', False):
                        widgets.append(it)
        elif self.mtype == '-l':
            for it in map:
                if isinstance(map[it], (dict)):
                    if map[it]["isBlock"] is False and map[it].get('isGPU', False) is False:
                        widgets.append(it)
        else:
            for it in map:
                if isinstance(map[it], (dict)):
                    if map[it]["isBlock"] is False:
                        widgets.append(it)
                else:
                    widgets.append(it)
        if '1c44470b-acc5-5ef7-a178-06f567e3ebab' in widgets:
            self.ext = 'serverimage'
        return widgets

    def markStop(self):
        print(f"   {self.name} waiting stop")
        self.is_running = False

    def remake(self):
        print(f"   {self.name} waiting stop")
        self.is_running = False
