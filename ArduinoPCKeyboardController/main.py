# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(250, 150)
#     w.setWindowTitle("Simple")
#     w.show()
#
#     sys.exit(app.exec_())

from HardwareKeyboard.HeadlessKeyboard import ArduinoHeadlessKeyboard

if __name__ == '__main__':
    HWKeyboard = ArduinoHeadlessKeyboard()
    HWKeyboard.autoconnect()
    HWKeyboard.execute_command()