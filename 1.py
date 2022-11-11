from typing import Literal


class Power:
    __slots__ = "amount"

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return str(self.amount) + "W"

    def __repr__(self) -> str:
        return str(self)

    def __int__(self) -> int:
        return self.amount


class MemoryUnit:
    __slots__ = ("unit", "amount")

    def __init__(self, unit: Literal["B", "KB", "MB", "GB", "TB"], amount: float):
        self.unit = unit
        self.amount = amount

    def __str__(self):
        return str(self.amount) + self.unit


class CPUMemoryStandard:
    __slots__ = ("standard", "channels", "max")

    def __init__(self, standard: Literal["DDR1", "DDR2", "DDR3", "DDR4", "DDR5"], channels: int, maximum: int) -> None:
        self.standard = standard
        self.channels = channels
        self.max = maximum

    def __str__(self) -> str:
        return self.standard + " | " + \
               str(self.channels) + " memory channels | " + \
               str(self.max) + "MHz - maximum memory speed"

    def __repr__(self) -> str:
        return str(self)


class GPUMemoryStandard:
    __slots__ = ("standard", "size", "bus", "bandwidth")

    def __init__(self,
                 standard: Literal["GDDR1", "GDDR2", "GDDR3", "GDDR4", "GDDR5"],
                 size: MemoryUnit,
                 bus: int,
                 bandwidth: MemoryUnit
                 ) -> None:
        self.standard = standard
        self.size = size
        self.bus = bus
        self.bandwidth = bandwidth

    def __str__(self) -> str:
        return self.standard + " | " + \
               str(self.size) + " VRAM | " + \
               str(self.bus) + "bit memory bus | " + \
               str(self.bandwidth) + "/s memory bandwidth"

    def __repr__(self) -> str:
        return str(self)


class Speed:
    __slots__ = ("base", "boost")

    def __init__(self, base: float, boost: float) -> None:
        self.base = base
        self.boost = boost

    def __str__(self) -> str:
        return str(self.base) + " - " + str(self.boost) + " GHz"

    def __repr__(self) -> str:
        return str(self)

    def __float__(self) -> float:
        return self.base


class GPUSpeed:
    __slots__ = "base"

    def __init__(self, base: int) -> None:
        self.base = base

    def __str__(self) -> str:
        return str(self.base) + "MHz"

    def __repr__(self) -> str:
        return str(self)

    def __int__(self) -> int:
        return self.base


class RWSpeed:
    __slots__ = ("read", "write")

    def __init__(self, read: MemoryUnit, write: MemoryUnit) -> None:
        self.read = read
        self.write = write

    def __str__(self) -> str:
        return str(self.read) + "/s (Read) | " + str(self.write) + "/s (Write)"

    def __repr__(self) -> str:
        return str(self)


class Cores:
    __slots__ = "amount"

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return str(self.amount) + " cores"

    def __repr__(self) -> str:
        return str(self)

    def __int__(self) -> int:
        return self.amount


class Cache:
    __slots__ = ("memory", "level")

    def __init__(self, memory: MemoryUnit, level: Literal[1, 2, 3]) -> None:
        self.memory = memory
        self.level = level

    def __str__(self) -> str:
        return "L" + str(self.level) + " - " + str(self.memory)

    def __repr__(self) -> str:
        return str(self)


class Caches:
    __slots__ = ("L1", "L2", "L3", "caches")

    def __init__(self, l1: Cache = None, l2: Cache = None, l3: Cache = None) -> None:
        self.L1 = l1
        self.L2 = l2
        self.L3 = l3
        self.caches = [self.L1, self.L2, self.L3]
        for cache in self.caches:
            if cache is None:
                self.caches.remove(cache)

    def __str__(self) -> str:
        built = ""
        for cache in self.caches:
            built += str(cache) + "\n"
        return built

    def __repr__(self) -> str:
        return str(self)


class Technology:
    __slots__ = "amount"

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return str(self.amount) + "nm"

    def __repr__(self) -> str:
        return str(self)

    def __int__(self) -> int:
        return self.amount


class CPU:
    cpu_speed = Speed(3.1, 3.4)
    cpu_cores = Cores(4)
    cpu_technology = Technology(14)
    cpu_tdp = Power(65)
    cpu_cache = Caches(
        Cache(MemoryUnit("KB", 384.0), 1),
        Cache(MemoryUnit("MB", 2.0), 2),
        Cache(MemoryUnit("MB", 8.0), 3)
    )
    cpu_name = "AMD Ryzen™ 3 1200"
    cpu_overclockable = True
    cpu_socket = "AM4"
    cpu_memory = CPUMemoryStandard("DDR4", 2, 2667)
    cpu_gpu = None

    def calculate(self):
        print("Calculating stuff")


class GPU:
    gpu_speed = GPUSpeed(459)
    gpu_technology = Technology(80)
    gpu_tdp = Power(30)
    gpu_cache = Caches(
        None,
        Cache(MemoryUnit("KB", 32.0), 2),
        None
    )
    gpu_name = "NVIDIA GeForce 8500 GT"
    gpu_overclockable = True
    gpu_memory = GPUMemoryStandard(
                                   "GDDR4",
                                   MemoryUnit("MB", 256.0),
                                   128,
                                   MemoryUnit("GB", 12.80)
                                   )

    def render(self):
        print("rendering stuff")


class Monitor:
    monitor_refreshrate = 60
    monitor_resolution = "1920x1080"
    monitor_size = '21.5"'

    def display(self):
        print("displaying stuff")


class SSD:
    ssd_size = MemoryUnit("GB", 480.0)
    ssd_name = "Kingston A400"
    ssd_interface = "SATA 3.0/2.0"
    ssd_speed = RWSpeed(
        MemoryUnit("MB", 500),
        MemoryUnit("MB", 450)
    )
    ssd_written = None

    def write(self, data):
        self.ssd_written = data

    def read(self):
        return self.ssd_written


class RAM:
    ram_size = MemoryUnit("GB", 8.0)
    ram_written = None

    def r_write(self, data):
        self.ram_written = data

    def r_read(self):
        return self.ram_written


class Computer(CPU, GPU, Monitor, SSD, RAM):
    ...


my_pc = Computer()
my_pc.calculate()
my_pc.render()
my_pc.display()
print(my_pc.read())
my_pc.write("Test!")
print(my_pc.read())
print(my_pc.r_read())
my_pc.r_write("Test 2!")
print(my_pc.r_read())

