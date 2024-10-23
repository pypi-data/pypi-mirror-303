from collections import defaultdict
import psutil
import os
import time
import requests
import socket
from robometrics.models.metrics import StaticMachine, MachineInfo, ProcessInfo

nvml = True
try:
    from pynvml import *
except ImportError:
    nvml = False
    print("Warning: pynvml not found. GPU monitoring will be disabled.")


class Worker(object):
    machine: StaticMachine
    watching_processes: list[int] = []
    watching_processes_ocupied: bool = False
    machine_id: str = ""
    server_url: str | None = None
    alone: bool = True

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Worker, cls).__new__(cls)
        return cls.instance

    def __init__(self, server_url: str | None = None):
        self.server_url = server_url
        if server_url is None:
            self.alone = True
        else:
            self.alone = self.testServerState()
        nvmlInit()
        self.machine = self.get_static_machine_info()
        nvmlInit()
        self.gpu_handle = nvmlDeviceGetHandleByIndex(0)
        self.machine_id = self.getMachineId()
        self.post_machine()
        # self.watching_processes = []

    def testServerState(self):
        try:
            requests.get(self.server_url + "/health")
        except Exception as _:
            self.prepare_csvs()
            return False
        return True

    def prepare_csvs(self):
        if not os.path.exists("./async/static.csv"):
            with open("./async/static.csv", "w") as f:
                f.write(
                    "machine_id,cpu_count,cpu_freq,total_memory,total_gpu_memory,gpu_name,gpu_count,gpu_driver_version,gpu_memory,created_at\n")
        if not os.path.exists("./async/machine.csv"):
            with open("./async/machine.csv", "w") as f:
                f.write(
                    "machine_id,cpu_percent,memory_percent,gpu_percent,gpu_memory_percent,cpu_temp,gpu_temp,gpu_fan_speed,gpu_power_usage,created_at\n")
        if not os.path.exists("./async/processes.csv"):
            with open("./async/processes.csv", "w") as f:
                f.write(
                    "pid,name,cpu_percent,memory_percent,gpu_memory,gpu_memory_percent,status,create_time,num_threads,threads,ParentProcess,created_at\n")

    @staticmethod
    def getMachineId():
        hostname = socket.gethostname()
        return hostname

    def post_machine(self):
        createdAt = time.time()
        if self.alone:
            with open("./async/static.csv", "a") as f:
                f.write(f'"{self.machine_id}","{self.machine.cpu_count}","{self.machine.cpu_freq}","{self.machine.total_memory}","{self.machine.total_gpu_memory}","{self.machine.gpu_name}","{self.machine.gpu_count}","{self.machine.gpu_driver_version}","{self.machine.gpu_memory}","{createdAt}"\n')
            return
        d = self.machine.model_dump()
        d["created_at"] = createdAt
        requests.post(self.server_url + "/intake/static_machine/" + self.machine_id,
                      json=d, headers={"Content-Type": "application/json"})

    @staticmethod
    def get_static_machine_info():
        if not nvml:
            return StaticMachine(
                cpu_count=os.cpu_count(),
                cpu_freq=psutil.cpu_freq().current,
                total_memory=psutil.virtual_memory().total / 1024 ** 3,
                total_gpu_memory=0,
                gpu_name="",
                gpu_count=0,
                gpu_driver_version="",
                gpu_memory=0
            )
        device_count = nvmlDeviceGetCount()
        device = nvmlDeviceGetHandleByIndex(0)
        gpu_name = nvmlDeviceGetName(device)
        gpu_driver_version = nvmlSystemGetDriverVersion()
        gpu_memory = nvmlDeviceGetMemoryInfo(device).total / 1024 ** 2
        nvmlShutdown()
        return StaticMachine(
            cpu_count=os.cpu_count(),
            cpu_freq=psutil.cpu_freq().current,
            total_memory=psutil.virtual_memory().total / 1024 ** 3,
            total_gpu_memory=gpu_memory,
            gpu_name=gpu_name,
            gpu_count=device_count,
            gpu_driver_version=gpu_driver_version,
            gpu_memory=gpu_memory
        )

    @classmethod
    def add_process(cls, pid: int):
        while cls.watching_processes_ocupied:
            time.sleep(0.1)
        cls.watching_processes_ocupied = True
        if pid not in cls.watching_processes:
            cls.watching_processes.append(pid)
        cls.watching_processes_ocupied = False

    @classmethod
    def unregister_process(cls, pid: int):
        while cls.watching_processes_ocupied:
            time.sleep(0.1)
        cls.watching_processes_ocupied = True
        try:
            cls.watching_processes.remove(pid)
        except ValueError:
            pass
        cls.watching_processes_ocupied = False

    def get_machine_info(self):
        nvmlInit()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        if not nvml:
            return MachineInfo(
                cpu_percent=cpu_percent,
                memory_percent=memory_percent,
                gpu_percent=0,
                gpu_memory_percent=0,
                cpu_temp=None,
                gpu_temp=None,
                gpu_fan_speed=None,
                gpu_power_usage=None
            )
        gpu_memory = nvmlDeviceGetMemoryInfo(self.gpu_handle)
        gpu_percent = gpu_memory.used / (gpu_memory.total + 1)
        gpu_temp = nvmlDeviceGetTemperature(
            self.gpu_handle, NVML_TEMPERATURE_GPU)
        try:
            gpu_fan_speed = nvmlDeviceGetFanSpeed(self.gpu_handle)
        except NVMLError:
            gpu_fan_speed = None
        gpu_power_usage = nvmlDeviceGetPowerUsage(self.gpu_handle)
        cpu_temp = psutil.sensors_temperatures().get('coretemp', None)
        if cpu_temp:
            cpu_temp = cpu_temp[0].current
        return MachineInfo(
            cpu_percent=cpu_percent,
            memory_percent=memory_percent,
            gpu_percent=gpu_percent,
            gpu_memory_percent=gpu_memory.used / (gpu_memory.total + 1),
            cpu_temp=cpu_temp,
            gpu_temp=gpu_temp,
            gpu_fan_speed=gpu_fan_speed,
            gpu_power_usage=gpu_power_usage
        )

    def get_processes(self) -> list[ProcessInfo]:
        processes_gpu_info = self.preload_gpu_process_info()
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status', 'create_time', 'num_threads', 'threads']):
            try:
                if proc.info['pid'] not in self.watching_processes:
                    continue
                pinfo = proc.info
                processes.append(ProcessInfo(
                    pid=pinfo['pid'],
                    name=pinfo['name'],
                    cpu_percent=pinfo['cpu_percent'],
                    memory_percent=pinfo['memory_percent'],
                    status=pinfo['status'],
                    create_time=pinfo['create_time'],
                    num_threads=pinfo['num_threads'],
                    threads=[thread.id for thread in pinfo['threads']],
                    gpu_memory=processes_gpu_info.get(pinfo['pid'], 0),
                    gpu_memory_percent=processes_gpu_info.get(
                        pinfo['pid'], 0) / (self.machine.gpu_memory + 1),
                    ParentProcess=None
                ))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return processes

    def preload_gpu_process_info(self) -> dict[int, int]:
        if not nvml:
            return {}
        processes = nvmlDeviceGetComputeRunningProcesses(self.gpu_handle)
        processes_gpu_info = defaultdict(int)
        for process in processes:
            processes_gpu_info[process.pid] = process.usedGpuMemory
        return processes_gpu_info

    def register_records(self, machine: MachineInfo, processes: list[ProcessInfo]):
        createdAt = time.time()
        if not self.alone:
            d = machine.model_dump()
            d["created_at"] = createdAt
            try:
                requests.post(self.server_url + "/intake/machine/" + self.machine_id,
                              json=d, headers={"Content-Type": "application/json"})
            except Exception as e:
                print(e)
            ps = [process.model_dump() for process in processes]
            for p in ps:
                p["created_at"] = createdAt
            try:
                requests.post(self.server_url + "/intake/processes/" + self.machine_id,
                              json=[process.model_dump() for process in processes], headers={"Content-Type": "application/json"})
            except Exception as e:
                print(e)
        else:
            with open("./async/machine.csv", "a") as f:
                f.write(f'"{self.machine_id}","{machine.cpu_percent}","{machine.memory_percent}","{machine.gpu_percent}","{machine.gpu_memory_percent}","{machine.cpu_temp}","{machine.gpu_temp}","{machine.gpu_fan_speed}","{machine.gpu_power_usage}","{createdAt}"\n')
            with open("./async/processes.csv", "a") as f:
                for process in processes:
                    f.write(f'"{process.pid}","{process.name}","{process.cpu_percent}","{process.memory_percent}","{process.gpu_memory}","{process.gpu_memory_percent}","{process.status}","{process.create_time}","{process.num_threads}","{process.threads}","{process.ParentProcess}","{createdAt}"\n')

    def run_continuously(self):
        while True:
            MachineRecord = self.get_machine_info()
            ProcessRecord = self.get_processes()
            print(MachineRecord)
            print(ProcessRecord)
            self.register_records(MachineRecord, ProcessRecord)
            time.sleep(1)

    def run_pipe(self):
        if (os.path.exists("/tmp/worker")):
            os.remove("/tmp/worker")
        os.mkfifo("/tmp/worker")
        print("Hearing")
        while True:
            time.sleep(0.1)
            with open("/tmp/worker", "r") as fifo:
                data = fifo.read()
                if data and len(data) > 0:
                    try:
                        pid = int(data)
                        if pid < 0:
                            self.unregister_process(-pid)
                        else:
                            self.add_process(pid)
                    except ValueError:
                        pass
            time.sleep(0.1)


def sync():
    import sys
    args = sys.argv
    machine_id = Worker.getMachineId()
    if len(args) > 1:
        server_url = args[1]
    else:
        print("Usage: python worker.py <server_url>")
        return
    if not os.path.exists("./async/static.csv"):
        print("No static.csv found skipping sync for static.csv")
    else:
        with open("./async/static.csv", "r") as f:
            data = f.read()
        if len(data) > 0:
            data = data.split("\n")[1]
            record = StaticMachine(
                cpu_count=int(data[1]),
                cpu_freq=float(data[2]),
                total_memory=float(data[3]),
                total_gpu_memory=float(data[4]),
                gpu_name=data[5],
                gpu_count=int(data[6]),
                gpu_driver_version=data[7],
                gpu_memory=float(data[8]),
                created_at=float(data[9])
            )
            requests.post(server_url + "/intake/static_machine" + machine_id,
                          data=record, headers={"Content-Type": "text/csv"})
        os.remove("./async/static.csv")
    if not os.path.exists("./async/machine.csv"):
        print("No machine.csv found skipping sync for machine.csv")
    else:
        with open("./async/machine.csv", "r") as f:
            data = f.read()
        if len(data) > 0:
            data = data.split("\n")[1:]
            records = []
            for record in data:
                record = record.split(",")
                records.append(MachineInfo(
                    cpu_percent=float(record[1]),
                    memory_percent=float(record[2]),
                    gpu_percent=float(record[3]),
                    gpu_memory_percent=float(record[4]),
                    cpu_temp=float(record[5]),
                    gpu_temp=float(record[6]),
                    gpu_fan_speed=float(record[7]),
                    gpu_power_usage=float(record[8]),
                    created_at=float(record[9])
                ))
            requests.post(server_url + "/intake/many/machine" + machine_id,
                          data=records, headers={"Content-Type": "text/csv"})
        os.remove("./async/machine.csv")
    if not os.path.exists("./async/processes.csv"):
        print("No processes.csv found skipping sync for processes.csv")
    else:
        with open("./async/processes.csv", "r") as f:
            data = f.read()
        if len(data) > 0:
            data = data.split("\n")[1:]
            records = []
            for record in data:
                record = record.split(",")
                records.append(ProcessInfo(
                    pid=int(record[0]),
                    name=record[1],
                    cpu_percent=float(record[2]),
                    memory_percent=float(record[3]),
                    gpu_memory=int(record[4]),
                    gpu_memory_percent=float(record[5]),
                    status=record[6],
                    create_time=float(record[7]),
                    num_threads=int(record[8]),
                    threads=[int(thread) for thread in record[9].split()],
                    ParentProcess=int(record[10]),
                    created_at=float(record[11])
                ))
            requests.post(server_url + "/intake/many/processes" + machine_id,
                          data=records, headers={"Content-Type": "text/csv"})
        os.remove("./async/processes.csv")


def main():
    import threading
    import sys
    args = sys.argv
    if len(args) > 1:
        server_url = args[1]
    else:
        server_url = None
    w = Worker(server_url)
    t1 = threading.Thread(target=w.run_pipe)
    t2 = threading.Thread(target=w.run_continuously)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
