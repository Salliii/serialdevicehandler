import serial
import os


class SerialDeviceHandler(object):    
    def __init__(self, port=None, baudrate=None, timeout=None) -> None:
        
        self.serial_interface = serial.Serial()
        self.serial_interface.port = str( port if port != None else ("COM1" if os.name == "nt" else "/dev/tty") )
        self.serial_interface.baudrate = str( baudrate if baudrate != None else "9600" )
        self.serial_interface.timeout = float( max(timeout, 0.2) if timeout != None else 0.2 )