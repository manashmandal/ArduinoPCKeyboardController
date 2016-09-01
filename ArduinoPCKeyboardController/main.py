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
        self.ui.connectButton.setEnabled(True)
        self.ui.disconnectButton.setEnabled(False)

        # Variables
        self.baud = 9600
        self.portName = ''
        self.arduino_board_details = ''
        # Baudrates
        self.baud_rates = ['4800', '9600', '14400', '19200', '28800', '38400', '57600', '115200']

        # Adding baudrates
        self.ui.baudRateComboBox.addItems(self.baud_rates)


        self.ui.baudRateComboBox.setCurrentText('9600')


        #Connections
        self.ui.baudRateComboBox.currentIndexChanged.connect(self.get_baud)
        self.ui.findArduinoButton.clicked.connect(self.find_arduino)
        self.ui.comportComboBox.currentIndexChanged.connect(self.select_port)
        self.ui.connectButton.clicked.connect(self.connect_)
        self.ui.disconnectButton.clicked.connect(self.disconnect_)
        self.ui.autoConnectButton.clicked.connect(self.autoconnect)

    def connect_keyboard(self):
        print("Connect Button Clicked")

    def get_baud(self, current_baud):
        baud = int(self.baud_rates[current_baud])
        print(baud)

    def find_arduino(self):
        self.ui.statusLabel.setText("Finding Arduino")
        details = self.HWKeyboard.get_arduino_port()
        if details != "":
            print (details[1])
            self.arduino_board_details = details[1]
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

    def connect_(self):
        if self.portName != '':
            self.HWKeyboard.set_port(self.portName)
            self.HWKeyboard.set_baud(self.baud)
            self.HWKeyboard.connect()
        else:
            self.ui.statusLabel.setText("Port not selected")
        if self.HWKeyboard.is_connected():
            self.ui.statusLabel.setText("Connected")
            self.ui.connectButton.setEnabled(False)
            self.ui.disconnectButton.setEnabled(True)
        else:
            self.ui.statusLabel.setText("Connection Failed! Check COM Port")


    def disconnect_(self):
        self.HWKeyboard.disconnect()
        self.ui.statusLabel.setText("Disconnected Arduino")
        self.ui.disconnectButton.setEnabled(False)
        self.ui.connectButton.setEnabled(True)
        self.ui.findArduinoButton.setEnabled(True)

    def autoconnect(self):
        self.HWKeyboard.disconnect()
        self.HWKeyboard.autoconnect()
        if self.HWKeyboard.is_connected():
            self.ui.findArduinoButton.setEnabled(False)
            self.ui.disconnectButton.setEnabled(True)
            self.ui.connectButton.setEnabled(False)
            self.ui.statusLabel.setText("Connected :" + self.HWKeyboard.get_arduino_details())
        # self.ui.statusLabel.setText(self.HWKeyboard.get_arduino_details())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboardGUI = KeyboardControllerGUI()
    keyboardGUI.show()
    try:
        sys.exit(app.exec_())
    except:
        print("exiting")
    # HWKeyboard = ArduinoHeadlessKeyboard()
    # HWKeyboard.autoconnect()
    # HWKeyboard.execute_command()