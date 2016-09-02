# Arduino PC Keyboard Controller
PC Keyboard control by Arduino


# Screenshot

![ui](Screenshots/mainui.png)

# How To

* Download the repository
* [Interface a keypad with your arduino board](http://playground.arduino.cc/Main/KeypadTutorial)
* Modify and upload the arduino code
  * You can add more keypad functions. [See here](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)
* Run `main.py` then establish serial communication by clicking `Autoconnect` or `Connect`
* Check `Auto Execute Commands` for executing keyboard command automatically
  * Or you can grab the latest command manually by clicking `Read Command` Button

# Building From Source

Currently binary file is not available so you have to build it from source. Following libraries and frameworks should be installed before building.

## Python Dependencies

* [Python 3](https://www.python.org/download/releases/3.0/)
* [PyQt5](https://pypi.python.org/pypi/PyQt5)
* [PyAutoGui](https://pyautogui.readthedocs.io/)
* [pySerial](https://pythonhosted.org/pyserial/)


# Any Questions?

You can always open an issue if you face any problems running the application. Contributors are welcome to contribute. 
