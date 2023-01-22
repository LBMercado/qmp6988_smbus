from abc import ABC, abstractmethod
from enum import Enum

class I2cInterface(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def open(self, bus_no: int, address: str):
        pass
    
    @abstractmethod
    def read(self, reg: int, byte_count: int):
        pass
    
    @abstractmethod
    def write(self, reg: int, bytes_val: list[bytes]):
        pass
    
    @abstractmethod
    def close(self):
        pass