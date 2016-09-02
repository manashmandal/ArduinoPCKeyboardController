import serial
from serial.tools import list_ports

class Controller:
    def __init__(self, port='', baud=9600):
        self.port = port
        self.baud = baud
        self.data = ''
        self.arduino = serial.Serial()

    def set_port(self, port):
        self.port = port

    def set_baud(self, baud):
        self.baud = baud

    def connect(self):
        self.arduino = serial.Serial(self.port, baudrate=self.baud)
        self.disconnect()
        self.arduino.open()

    def disconnect(self):
        self.arduino.close()

    def is_open(self):
        return self.arduino.is_open

    # Returns True on successful data tx
    def write(self, data):
        # Converts string to byte array
        data_bytearray = bytearray(data, 'ascii')
        if self.is_open():
            self.arduino.write(data_bytearray)
            return True
        return False

    def readline(self):
        self.data = self.arduino.readline()
        return self.data

    def get_arduino_details(self):
        arduino_ports = [(_dev.device, _dev.description) for _dev in list_ports.comports() if _dev.description.__contains__("Arduino")]
        if len(arduino_ports) == 0:
            return ""
        return arduino_ports[0]

    def autoconnect(self):
        arduino_ports = [_dev.device for _dev in list_ports.comports() if _dev.description.__contains__("Arduino")]
        if len(arduino_ports) == 0:
            print("No Arduino Found! Check connection!")
            return False
        self.port = arduino_ports[0]
        print(self.port)
        self.set_port(str(self.port))
        self.connect()
