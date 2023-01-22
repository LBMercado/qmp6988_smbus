from piqmp6988.i2c_intf import I2cInterface
from smbus import SMBus

class Smbus(I2cInterface):
    def __init__(self):
        self.bus: SMBus = None
        self.bus_no: int = None
        self.address: int = None
        self.is_active: bool = False
    
    def open(self, bus_no: int, address: str):
        if self.bus is None or self.bus_no != bus_no:
            self.bus_no = bus_no
            self.close()
            self.bus = SMBus(bus_no)
            self.address = int(address)
            self.is_active = True
        elif not self.is_active:
            self.bus.open(self.bus_no)
            self.is_active = True
            
    
    def read(self, reg: int, byte_count: int):
        if not self.is_active:
            return
        data = self.bus.read_i2c_block_data(self.address, reg, byte_count)
        return (len(data), data)
    
    def write(self, reg: int, bytes_val: list[bytes]):
        if not self.is_active:
            return
        return self.bus.write_i2c_block_data(self.address, reg, bytes_val)
    
    def close(self):
        if self.is_active and self.bus is not None:
            self.bus.close()
            self.is_active = False