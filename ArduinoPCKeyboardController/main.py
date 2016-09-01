import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

from HardwareKeyboard.HeadlessKeyboard import ArduinoHeadlessKeyboard
from Interfaces.Ui_MainDialog import Ui_Dialog


class SerialReadThread(QThread):
    send_command = pyqtSignal('QString')

    def __init__(self, HWKbd):
        QThread.__init__(self)
        self.HWKbd = HWKbd

    def get_serial_data(self):
        self.HWKbd.get_command()
        return self.HWKbd.get_last_command()

    def run(self):
        self.sleep(5)
        while True:
            self.cmd = self.get_serial_data()
            self.send_command.emit(self.cmd)

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
        self.autoExec = False

        # Variables
        self.baud = 9600
        self.portName = ''
        self.arduino_board_details = ''
        # Baudrates
        self.baud_rates = ['4800', '9600', '14400', '19200', '28800', '38400', '57600', '115200']
        self.command = ''

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
        self.ui.autoExecCheckBox.clicked.connect(self.auto_execute)
        self.ui.readCommandButton.clicked.connect(self.read_command)
        self.ui.executeLatestCommandButton.clicked.connect(self.execute_command)

        self.serialThread = SerialReadThread(self.HWKeyboard)
        self.serialThread.send_command.connect(self.read_command_from_thread)

    @pyqtSlot(str)
    def read_command_from_thread(self, cmd):
        print(cmd)

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

    def auto_execute(self, bool):
        self.autoExec = bool
        if self.autoExec:
            self.serialThread.start()
        else:
            self.serialThread.terminate()


    def read_command(self):
        self.HWKeyboard.get_command()
        self.command = self.HWKeyboard.command
        print (self.command)

    def execute_command(self, cmd):
        self.HWKeyboard.exec_command(cmd)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboardGUI = KeyboardControllerGUI()
    keyboardGUI.show()
    keyboardGUI.read_command()
    try:
        sys.exit(app.exec_())
    except:
        print("exiting")
