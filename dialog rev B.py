# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#put following lines in separate file ?
import time;
from psuedoSensor import PseudoSensor
ps = PseudoSensor()
alarmOn = False
#

class MyDialog(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 508)
        self.singleRead = QtWidgets.QPushButton(Form)
        self.singleRead.setGeometry(QtCore.QRect(70, 20, 99, 30))
        self.singleRead.setAutoDefault(False)
        self.singleRead.setDefault(False)
        self.singleRead.setObjectName("singleRead")
        self.singleRead.clicked.connect(self.singleReadAction)
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
        self.read10.clicked.connect(self.read10Action)
        self.average = QtWidgets.QPushButton(Form)
        self.average.setGeometry(QtCore.QRect(310, 20, 99, 30))
        self.average.setObjectName("average")
        self.average.clicked.connect(self.averageAction)
        self.close = QtWidgets.QPushButton(Form)
        self.close.setGeometry(QtCore.QRect(440, 20, 99, 30))
        self.close.setObjectName("close")
        self.close.clicked.connect(self.closeAction)
        self.displayValues = QtWidgets.QTextBrowser(Form)
        self.displayValues.setGeometry(QtCore.QRect(60, 170, 481, 321))
        self.displayValues.setObjectName("displayValues")
        self.alarmOnOff = QtWidgets.QPushButton(Form)
        self.alarmOnOff.setGeometry(QtCore.QRect(270, 90, 81, 30))
        self.alarmOnOff.setObjectName("alarmOnOff")
        self.alarmOnOff.clicked.connect(self.alarmOnOffAction)
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
        self.enterTmpAlrm.setGeometry(QtCore.QRect(410, 90, 71, 32))
        self.enterTmpAlrm.setDecimals(1)
        self.enterTmpAlrm.setMinimum(-20.0)
        self.enterTmpAlrm.setSingleStep(0.1)
        self.enterTmpAlrm.setProperty("value", 75.0)
        self.enterTmpAlrm.setObjectName("enterTmpAlrm")

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
        self.alarmOnOff.setText(_translate("Form", "Alarm On"))
        self.tempLabel.setText(_translate("Form", "<html><head/><body><p>Hmdty  Tmp</p></body></html>"))
        self.commentLabel.setText(_translate("Form", "<html><head/><body><p>Comment</p></body></html>"))

# put following code in seperate file?
    def singleReadAction(MyDialog):
        ts = time.gmtime()
        h,t = ps.generate_values()
        displayStr = time.strftime("%Y-%m-%d %H:%M:%S   ",ts) + str(round(h,1)) + "%  " + str(round(t,1)) \
                     + " deg  Single Read"
        MyDialog.displayValues.append(displayStr)

    def read10Action(MyDialog):
        print("in Mydialog")
        for i in range(1,10):
            print("in loop")
            ts = time.gmtime()
            h,t = ps.generate_values()
            displayStr = time.strftime("%Y-%m-%d %H:%M:%S   ",ts) + str(round(h,1)) + "%  " + str(round(t,1)) \
                         + " deg  Reading " + str(i)
            MyDialog.displayValues.append(displayStr)
            time.sleep(1)
        displayStr = time.strftime("%Y-%m-%d %H:%M:%S   ",ts) + str(round(h,1)) + "%  " + str(round(t,1)) \
                     + " deg  Reading " + str(i+1) + " Done"
        MyDialog.displayValues.append(displayStr)

    def averageAction(MyDialog):
        hSum = 0
        hMin = 101.0
        hMax = -.1
        tSum = 0
        tMin = 101.0
        tMax = -21.0
        for ii in range(1,10):
            tss = time.gmtime()
            hh,tt = ps.generate_values()
            hSum = hh + hSum
            tSum = tt + tSum
            
            if tt > tMax:
                tMax = tt
            if hh > hMax:
                hMax = hh
            if hh < hMin:
                hMin = hh
            if tt < tMin:
                tMin = tt
                  
            displayStr = time.strftime("%Y-%m-%d %H:%M:%S   ",tss) + str(round(hh,1)) + "%  " \
                         + str(round(tt,1)) + " deg  Reading " + str(ii)
            MyDialog.displayValues.append(displayStr)
            time.sleep(1)

        displayStr = time.strftime("%Y-%m-%d %H:%M:%S   ",tss) + str(round(hh,1)) + "%  " \
                     + str(round(tt,1)) + " deg  Reading " + str(ii+1) + " Done"
        MyDialog.displayValues.append(displayStr)
    
        hAvg = hSum/10
        tAvg = tSum/10

#Display the average humidity and temperature
        displayStr = time.strftime("%Y-%m-%d %H:%M:%S   ",tss) + str(round(hAvg,1)) + \
                     "%  Avg  " + str(round(tAvg,1)) + " deg  Avg"
        MyDialog.displayValues.append(displayStr)
        
#Display the minimum humidity and temperature
        displayStr = time.strftime("%Y-%m-%d %H:%M:%S   ",tss) + str(round(hMin,1)) + \
                     "%  Min  " + str(round(tMin,1)) + " deg  Min"
        MyDialog.displayValues.append(displayStr)

#Display the maximum humidity and temperature
        displayStr = time.strftime("%Y-%m-%d %H:%M:%S   ",tss) + str(round(hMax,1)) + \
                     "%  Max  " + str(round(tMax,1)) + " deg  Max"
        MyDialog.displayValues.append(displayStr)

#Close the application
        def closeAction():
            sys.exit(app.exec_())

#This turns the humidity and temperature alarms on and off
        def alarmOnOffAction():
            if alarmOn ==  False:
                alarmOn = True
                MyDialog.alarmOnOff.setText(_translate("Form", "Alarm Off"))
            if alarmOn ==  True:
                alarmOn = False
                MyDialog.alarmOnOff.setText(_translate("Form", "Alarm On"))
            

                
        
