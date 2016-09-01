import pyautogui as keyboard
from SerialHandler.ArduinoController import Controller


class ArduinoHeadlessKeyboard:
    def __init__(self):
        self.arduino = Controller()
        self.command = ''

    def autoconnect(self):
        self.arduino.autoconnect()

    def set_baud(self, baud):
        self.arduino.set_baud(baud)

    def set_port(self, port):
        self.arduino.set_port(port)

    def disconnect(self):
        self.arduino.disconnect()

    def connect(self):
        self.arduino.connect()
        return self.arduino.is_open()

    def execute_command(self):
        if self.arduino.is_open():
            self.command = self.arduino.readline()
            # Remove the trailing newline
            self.command = self.command[:len(self.command)-1]
            # Convert byte to regular string
            self.command = str(self.command, 'utf-8')
            keyboard.press(self.command)
            return True
        print("Arduino Connection Error! Reconnect arduino and try again")
        return False

    def get_last_command(self):
        return self.command

    def get_arduino_details(self):
        return self.arduino.get_arduino_details()



if __name__ == '__main__':
    kbd = ArduinoHeadlessKeyboard()
    print (kbd.get_arduino_details())