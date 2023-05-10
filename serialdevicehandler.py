import serial
import os


class SerialDeviceHandler(object):    
    def __init__(self, port=None, baudrate=None, timeout=None) -> None:

        self.serial_interface = serial.Serial()
        self.serial_interface.port = str( port if port != None else ("COM1" if os.name == "nt" else "/dev/tty") )
        self.serial_interface.baudrate = str( baudrate if baudrate != None else "9600" )
        self.serial_interface.timeout = float( max(timeout, 0.2) if timeout != None else 0.2 )

        self.buffer = str()
        self.is_open = bool()
        self.is_executing = bool()
        self.eol_delimiter = str("\n")

        self.total_rx = int(0)
        self.total_tx = int(0)

    
    def __open__(self) -> int:
        """ open port """

        if not self.is_open:
            self.serial_interface.open()
            self.is_open = True
            return 1
        return 0
    

    def __close__(self) -> int:
        """ close port """

        if self.is_open:
            self.serial_interface.close()
            self.is_open = False
            return 1
        return 0
    

    def __readline__(self) -> bytes:
        """ read line """

        linebuffer = bytes()

        while len(linebuffer.decode("unicode-escape").split(self.eol_delimiter)) == 1:
            byte_in = self.serial_interface.read()

            if byte_in == b"":
                break

            linebuffer += byte_in
            self.total_rx += len(byte_in)

        return linebuffer