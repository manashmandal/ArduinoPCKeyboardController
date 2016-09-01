# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 109)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.comportHBoxLayout = QtWidgets.QHBoxLayout()
        self.comportHBoxLayout.setObjectName("comportHBoxLayout")
        self.comportLabel = QtWidgets.QLabel(Dialog)
        self.comportLabel.setObjectName("comportLabel")
        self.comportHBoxLayout.addWidget(self.comportLabel)
        self.comportComboBox = QtWidgets.QComboBox(Dialog)
        self.comportComboBox.setObjectName("comportComboBox")
        self.comportHBoxLayout.addWidget(self.comportComboBox)
        self.gridLayout.addLayout(self.comportHBoxLayout, 0, 0, 1, 1)
        self.baudRateHBoxLayout = QtWidgets.QHBoxLayout()
        self.baudRateHBoxLayout.setObjectName("baudRateHBoxLayout")
        self.baudRateLabel = QtWidgets.QLabel(Dialog)
        self.baudRateLabel.setObjectName("baudRateLabel")
        self.baudRateHBoxLayout.addWidget(self.baudRateLabel)
        self.baudRateComboBox = QtWidgets.QComboBox(Dialog)
        self.baudRateComboBox.setObjectName("baudRateComboBox")
        self.baudRateHBoxLayout.addWidget(self.baudRateComboBox)
        self.gridLayout.addLayout(self.baudRateHBoxLayout, 0, 1, 1, 1)
        self.pushButtonHBoxLayout = QtWidgets.QHBoxLayout()
        self.pushButtonHBoxLayout.setObjectName("pushButtonHBoxLayout")
        self.connectButton = QtWidgets.QPushButton(Dialog)
        self.connectButton.setObjectName("connectButton")
        self.pushButtonHBoxLayout.addWidget(self.connectButton)
        self.disconnectButton = QtWidgets.QPushButton(Dialog)
        self.disconnectButton.setObjectName("disconnectButton")
        self.pushButtonHBoxLayout.addWidget(self.disconnectButton)
        self.findArduinoButton = QtWidgets.QPushButton(Dialog)
        self.findArduinoButton.setObjectName("findArduinoButton")
        self.pushButtonHBoxLayout.addWidget(self.findArduinoButton)
        self.autoConnectButton = QtWidgets.QPushButton(Dialog)
        self.autoConnectButton.setObjectName("autoConnectButton")
        self.pushButtonHBoxLayout.addWidget(self.autoConnectButton)
        self.gridLayout.addLayout(self.pushButtonHBoxLayout, 1, 0, 1, 2)
        self.statusLabel = QtWidgets.QLabel(Dialog)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout.addWidget(self.statusLabel, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comportLabel.setText(_translate("Dialog", "COM Port"))
        self.baudRateLabel.setText(_translate("Dialog", "Baud Rate"))
        self.connectButton.setText(_translate("Dialog", "Connect"))
        self.disconnectButton.setText(_translate("Dialog", "Disconnect"))
        self.findArduinoButton.setText(_translate("Dialog", "Find Arduino"))
        self.autoConnectButton.setText(_translate("Dialog", "Autoconnect"))
        self.statusLabel.setText(_translate("Dialog", "Status"))

