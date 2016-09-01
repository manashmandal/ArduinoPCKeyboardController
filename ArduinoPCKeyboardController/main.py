import sys
from PyQt5.QtWidgets import QApplication, QDialog
from HardwareKeyboard.HeadlessKeyboard import ArduinoHeadlessKeyboard
from Interfaces.Ui_MainDialog import Ui_Dialog


class KeyboardControllerGUI(QDialog):
    def __init__(self):
        #init
        super(KeyboardControllerGUI, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.HWKeyboard = ArduinoHeadlessKeyboard()
        self.setWindowTitle("Arduino Keyboard Controller v0.0.1")
        self.is_connected = False

        # Variables
        self.baud = 9600
        self.portName = ''
        # Baudrates
        self.baud_rates = ['4800', '9600', '14400', '19200', '28800', '38400', '57600', '115200']

        # Adding baudrates
        self.ui.baudRateComboBox.addItems(self.baud_rates)


        self.ui.baudRateComboBox.setCurrentText('9600')


        #Connections
        self.ui.baudRateComboBox.currentIndexChanged.connect(self.get_baud)
        self.ui.findArduinoButton.clicked.connect(self.find_arduino)
        self.ui.comportComboBox.currentIndexChanged.connect(self.select_port)
        self.ui.connectButton.clicked.connect(self.connect)

    def connect_keyboard(self):
        print("Connect Button Clicked")

    def get_baud(self, current_baud):
        baud = int(self.baud_rates[current_baud])
        print(baud)

    def find_arduino(self):
        self.ui.statusLabel.setText("Finding Arduino")
        details = self.HWKeyboard.get_arduino_details()
        if details != "":
            print (details[1])
            self.ui.statusLabel.setText("Found: " + details[1] + " at " + details[0])
            ports = [self.ui.comportComboBox.itemText(i) for i in range(self.ui.comportComboBox.count())]
            if details[0] not in ports:
                self.ui.comportComboBox.addItem(details[0])
            self.portName = details[0]
            return True
        self.ui.statusLabel.setText("Not Found. Recheck Connection")
        return False

    def select_port(self, index):
        self.portName = self.ui.comportComboBox.itemText(index)
        print(self.portName)

    def connect(self):
        self.HWKeyboard.set_port(self.portName)
        self.HWKeyboard.set_baud(self.baud)
        self.is_connected = self.HWKeyboard.connect()
        print(self.is_connected)
        return self.is_connected

if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboardGUI = KeyboardControllerGUI()
    keyboardGUI.show()
    sys.exit(app.exec_())

    # HWKeyboard = ArduinoHeadlessKeyboard()
    # HWKeyboard.autoconnect()
    # HWKeyboard.execute_command()