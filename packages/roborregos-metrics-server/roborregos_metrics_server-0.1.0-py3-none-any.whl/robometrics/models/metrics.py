from pydantic import BaseModel
import time


class StaticMachine(BaseModel):
    cpu_count: int
    cpu_freq: float
    total_memory: float
    total_gpu_memory: float
    gpu_name: str
    gpu_count: int
    gpu_driver_version: str
    gpu_memory: float
    created_at: float = time.time()


class MachineInfo(BaseModel):
    cpu_percent: float
    memory_percent: float
    gpu_percent: float
    gpu_memory_percent: float
    cpu_temp: float | None
    gpu_temp: float | None
    gpu_fan_speed: float | None
    gpu_power_usage: int | None
    created_at: float = time.time()


class ProcessInfo(BaseModel):
    pid: int
    name: str
    cpu_percent: float
    memory_percent: float
    gpu_memory: int
    gpu_memory_percent: float
    status: str
    create_time: float
    num_threads: int
    threads: list[int]
    ParentProcess: int | None
    created_at: float = time.time()
