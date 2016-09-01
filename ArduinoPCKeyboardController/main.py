import sys
from PyQt5.QtWidgets import QApplication, QDialog
from HardwareKeyboard.HeadlessKeyboard import ArduinoHeadlessKeyboard
from Interfaces.Ui_MainDialog import Ui_Dialog


class KeyboardControllerGUI(QDialog):
    def __init__(self):
        super(KeyboardControllerGUI, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.HWKeyboard = None
        self.ui.connectButton.clicked.connect(self.connect_keyboard)
        # Variables
        self.baud = 9600

        # Baudrates
        self.baud_rates = ['4800', '9600', '14400', '19200', '28800', '38400', '57600', '115200']

        # Adding baudrates
        self.ui.baudRateComboBox.addItems(self.baud_rates)
        self.ui.baudRateComboBox.currentIndexChanged.connect(self.get_baud)

        self.ui.baudRateComboBox.setCurrentText('9600')

    def connect_keyboard(self):
        print("Connect Button Clicked")

    def get_baud(self, current_baud):
        baud = int(self.baud_rates[current_baud])
        print(baud)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboardGUI = KeyboardControllerGUI()
    keyboardGUI.show()
    sys.exit(app.exec_())

    # HWKeyboard = ArduinoHeadlessKeyboard()
    # HWKeyboard.autoconnect()
    # HWKeyboard.execute_command()