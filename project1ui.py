# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MyDialog(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 508)
        self.singleRead = QtWidgets.QPushButton(Form)
        self.singleRead.setGeometry(QtCore.QRect(70, 20, 99, 30))
        self.singleRead.setAutoDefault(False)
        self.singleRead.setDefault(False)
        self.singleRead.setObjectName("singleRead")
        self.timeLable = QtWidgets.QLabel(Form)
        self.timeLable.setGeometry(QtCore.QRect(80, 140, 68, 22))
        self.timeLable.setObjectName("timeLable")
        self.humidityAlarmLabel = QtWidgets.QLabel(Form)
        self.humidityAlarmLabel.setGeometry(QtCore.QRect(130, 60, 121, 22))
        self.humidityAlarmLabel.setObjectName("humidityAlarmLabel")
        self.TemperatureAlarmLabel = QtWidgets.QLabel(Form)
        self.TemperatureAlarmLabel.setGeometry(QtCore.QRect(380, 60, 151, 22))
        self.TemperatureAlarmLabel.setObjectName("TemperatureAlarmLabel")
        self.read10 = QtWidgets.QPushButton(Form)
        self.read10.setGeometry(QtCore.QRect(190, 20, 99, 30))
        self.read10.setObjectName("read10")
        self.average = QtWidgets.QPushButton(Form)
        self.average.setGeometry(QtCore.QRect(310, 20, 99, 30))
        self.average.setObjectName("average")
        self.close = QtWidgets.QPushButton(Form)
        self.close.setGeometry(QtCore.QRect(440, 20, 99, 30))
        self.close.setObjectName("close")
        self.displayValues = QtWidgets.QTextBrowser(Form)
        self.displayValues.setGeometry(QtCore.QRect(60, 170, 481, 321))
        self.displayValues.setObjectName("displayValues")
        self.tempLabel = QtWidgets.QLabel(Form)
        self.tempLabel.setGeometry(QtCore.QRect(270, 140, 101, 22))
        self.tempLabel.setObjectName("tempLabel")
        self.commentLabel = QtWidgets.QLabel(Form)
        self.commentLabel.setGeometry(QtCore.QRect(380, 140, 81, 22))
        self.commentLabel.setObjectName("commentLabel")
        self.enterHmdAlrm = QtWidgets.QDoubleSpinBox(Form)
        self.enterHmdAlrm.setGeometry(QtCore.QRect(150, 90, 71, 32))
        self.enterHmdAlrm.setDecimals(1)
        self.enterHmdAlrm.setMaximum(100.0)
        self.enterHmdAlrm.setSingleStep(0.1)
        self.enterHmdAlrm.setProperty("value", 75.0)
        self.enterHmdAlrm.setObjectName("enterHmdAlrm")
        self.enterTmpAlrm = QtWidgets.QDoubleSpinBox(Form)
        self.enterTmpAlrm.setGeometry(QtCore.QRect(420, 90, 71, 32))
        self.enterTmpAlrm.setDecimals(1)
        self.enterTmpAlrm.setMinimum(-20.0)
        self.enterTmpAlrm.setSingleStep(0.1)
        self.enterTmpAlrm.setProperty("value", 75.0)
        self.enterTmpAlrm.setObjectName("enterTmpAlrm")
        self.AlarmOnOff = QtWidgets.QRadioButton(Form)
        self.AlarmOnOff.setGeometry(QtCore.QRect(250, 90, 141, 27))
        self.AlarmOnOff.setObjectName("AlarmOnOff")
        self.AlarmOnOff.setChecked(False)
        self-AlarmOnOff.toggled.connect(self.onClicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Humidity-Temperature"))
        self.singleRead.setText(_translate("Form", "Single Read"))
        self.timeLable.setText(_translate("Form", "Time"))
        self.humidityAlarmLabel.setText(_translate("Form", "Humidity Alarm"))
        self.TemperatureAlarmLabel.setText(_translate("Form", "Temperature Alarm"))
        self.read10.setText(_translate("Form", "Read 10"))
        self.average.setText(_translate("Form", "Average"))
        self.close.setText(_translate("Form", "Close"))
        self.tempLabel.setText(_translate("Form", "<html><head/><body><p>Hmdty  Tmp</p></body></html>"))
        self.commentLabel.setText(_translate("Form", "<html><head/><body><p>Comment</p></body></html>"))
        self.AlarmOnOff.setText(_translate("Form", "Alarms On/Off"))

    def onClicked(MyDialog):
        MyDialog = self.sender()
        if MyDialog,isChecked():
            print("alarm on")
        else:
            print("alarm off")

