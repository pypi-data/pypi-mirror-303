from datetime import datetime
from socket import AddressFamily
import psutil
from .constants import UTC
from .tools import isAdmin, isWindows, gethostname
from .logger import debuglog
import platform
import shutil

class SensorStats:
    initialised: bool = False
    pids: "list[int]" = []
    pid_count: int = 0
    cpu_count: int = 0
    cpu_freq: float = 0
    cpu_utilisation: float = 0
    cpu_load_average_1min: float = 0
    cpu_load_average_5min: float = 0
    cpu_load_average_15min: float = 0
    memory_utilisation: float = 0
    memory_bytes_total: int = 0
    memory_bytes_used: int = 0
    network_bytes_sent: int = 0
    network_bytes_recv: int = 0
    network_errors_in: int = 0
    network_errors_out: int = 0
    network_drops_in: int = 0
    network_drops_out: int = 0
    network_total_errors_in: int = 0
    network_total_errors_out: int = 0
    network_total_drops_in: int = 0
    network_total_drops_out: int = 0
    os_name: str = None
    os_release: str = None
    os_version: str = None
    os_architecture: str = None
    root_fs_usage: float = 0
    temperature: float = 0
    __network_counters = None
    boot_time: datetime = None
    get_temperature: callable = None
    @classmethod
    def init_stats(cls):
        ...

    @classmethod
    def get_stats(cls):
        if cls.get_temperature is None:
            if isWindows():
                if isAdmin():
                    cls.get_temperature = cls.get_windows_temperature
                else:
                    cls.get_temperature = cls.get_unknown_temperature
            else:
                cls.get_temperature = cls.get_linux_temperature
        cls.pids = psutil.pids()
        cls.pid_count = len(cls.pids)
        cls.cpu_count = psutil.cpu_count()
        cls.cpu_freq = psutil.cpu_freq().current
        cls.cpu_utilisation = psutil.cpu_percent()
        cpuload = psutil.getloadavg()
        cls.cpu_load_average_1min = cpuload[0] / cls.cpu_count * 100
        cls.cpu_load_average_5min = cpuload[1] / cls.cpu_count * 100
        cls.cpu_load_average_15min = cpuload[2] / cls.cpu_count * 100

        vmem = psutil.virtual_memory()
        cls.memory_bytes_total = vmem.total
        cls.memory_bytes_used = vmem.used
        cls.memory_utilisation = vmem.percent

        if cls.__network_counters is None:
            cls.__network_counters = psutil.net_io_counters()
            cls.boot_time = datetime.fromtimestamp(
                psutil.boot_time(), tz=UTC).strftime("%Y%m%dT%H%M%S.%f+00:00")
        else:
            network_counters = psutil.net_io_counters()
            cls.network_bytes_sent: psutil.net_io_counters = cls.get_interval_value(cls.__network_counters.bytes_sent, network_counters.bytes_sent)
            cls.network_bytes_recv: psutil.net_io_counters = cls.get_interval_value(cls.__network_counters.bytes_recv, network_counters.bytes_recv)
            cls.network_errors_in: psutil.net_io_counters = cls.get_interval_value(cls.__network_counters.errin, network_counters.errin)
            cls.network_errors_out: psutil.net_io_counters = cls.get_interval_value(cls.__network_counters.errout, network_counters.errout)
            cls.network_drops_in: psutil.net_io_counters = cls.get_interval_value(cls.__network_counters.dropin, network_counters.dropin)
            cls.network_drops_out: psutil.net_io_counters = cls.get_interval_value(cls.__network_counters.dropout, network_counters.dropout)
            cls.__network_counters = network_counters

        cls.network_total_errors_in = cls.__network_counters.errin
        cls.network_total_errors_out = cls.__network_counters.errout
        cls.network_total_drops_in = cls.__network_counters.dropin
        cls.network_total_drops_out = cls.__network_counters.dropout

        cls.root_fs_usage = cls.get_root_usage()

        uname = platform.uname()
        cls.os_name = uname.system
        cls.os_release = uname.release
        cls.os_version = uname.version
        cls.os_architecture = uname.machine

        cls.get_temperature()
            
 
    @classmethod
    def get_interval_value(cls, oldvalue, newvalue) -> int:
        if oldvalue > newvalue:
            return newvalue
        return newvalue - oldvalue

    @classmethod
    def get_linux_temperature(cls):
        debuglog("Getting Linux Temperature")
        cls.temperature = 0

        if "sensors_temperatures" in dir(psutil):
            temperatures = psutil.sensors_temperatures()
            for key in ["cpu_thermal", "coretemp", "battery"]:
                if key in temperatures:
                    cls.temperature = temperatures[key][0].current
                    break
            else:
                for key, value in temperatures.items():
                    cls.temperature = value[0].current
                    break

    @classmethod
    def get_windows_temperature(cls):
        debuglog("Getting Windows Temperature - Not yet implemented")
        cls.temperature = 0

    @classmethod
    def get_unknown_temperature(cls):
        debuglog("Unable to retrieve Temperature")
        cls.temperature = 0

    @classmethod
    def get_root_usage(cls):
        usage = shutil.disk_usage("/")
        total_bytes = usage.total
        used_bytes = usage.used
        used = round(100 * used_bytes / total_bytes, 2)
        return used
    
    @classmethod
    def get_vip_addr(cls, fn_parms):
        vipaddr = cls.get_nic_addr(fn_parms)
        if vipaddr is None:
            return None
        return gethostname()

    @classmethod
    def get_nic_addr(cls, fn_parms):
        if fn_parms is None:
            raise ValueError(f"Error : NIC is missing fn_parms")
        nics = psutil.net_if_addrs()
        if fn_parms not in nics:
            return None
        
        nic = nics[fn_parms]
        for family, address, netmask, broadcast, ptp in nic:
            if family == AddressFamily.AF_INET:
                return address
        return None
