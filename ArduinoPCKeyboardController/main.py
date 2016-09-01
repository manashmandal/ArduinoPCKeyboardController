import sys
from PyQt5.QtWidgets import QApplication, QDialog
from HardwareKeyboard.HeadlessKeyboard import ArduinoHeadlessKeyboard
from Interfaces.Ui_MainDialog import Ui_Dialog


class KeyboardControllerGUI(QDialog):
    def __init__(self):
        super(KeyboardControllerGUI, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboardGUI = KeyboardControllerGUI()
    keyboardGUI.show()
    sys.exit(app.exec_())

    # HWKeyboard = ArduinoHeadlessKeyboard()
    # HWKeyboard.autoconnect()
    # HWKeyboard.execute_command()