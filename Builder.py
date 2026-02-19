"""
Definition: Build complex objects with many fields by repeatedly setting parameters
and then calling `build()` using a builder class.
It helps handle optional parameters and avoids constructor parameter explosion.
"""



from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Computer:
    cpu: Optional[str] = None
    ram: Optional[str] = None
    gpu: Optional[str] = None
    os: Optional[str] = None
    storage: Optional[str] = None



class ComputerBuilder:

    def __init__(self):
        self._pc = Computer()

    def set_cpu(self, cpu):
        self._pc.cpu = cpu
        return self
    
    def set_ram(self, ram):
        self._pc.ram = ram
        return self

    def set_gpu(self, gpu):
        self._pc.gpu = gpu
        return self

    def set_os(self, os):
        self._pc.os = os
        return self

    def add_storage(self, storage):
        self._pc.storage = storage
        return self
    
    def build(self):
        pc = self._pc
        self._pc = Computer()
        return pc



# ----- Director (optional but common) -----
class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_gaming_pc(self) -> Computer:
        return (self.builder
                .set_cpu("Ryzen 7 7800X3D")
                .set_ram("32")
                .add_storage("1TB NVMe SSD")
                .set_gpu("RTX 4080")
                .set_os("Windows 11")
                .build())

    def build_office_pc(self) -> Computer:
        return (self.builder
                .set_cpu("Core i5")
                .set_ram("16")
                .add_storage("512GB SSD")
                .set_os("Ubuntu")
                .build())


if __name__ == "__main__":

    custom_pc = ComputerBuilder().set_cpu("Core i9").set_gpu("4090").set_os("Ubuntu").set_ram("32").add_storage("1 TB").build()
    print(custom_pc)

    director = ComputerDirector(ComputerBuilder())

    gaming_pc = director.build_gaming_pc()
    print(gaming_pc)

    office_pc = director.build_office_pc()
    print(office_pc)