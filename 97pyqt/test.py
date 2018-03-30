# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 54, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 54, 12))
        self.label_2.setObjectName("label_2")
        self.input_value = QtWidgets.QLineEdit(self.centralwidget)
        self.input_value.setGeometry(QtCore.QRect(110, 90, 151, 20))
        self.input_value.setObjectName("input_value")
        self.output_value = QtWidgets.QLineEdit(self.centralwidget)
        self.output_value.setGeometry(QtCore.QRect(110, 120, 151, 20))
        self.output_value.setReadOnly(True)
        self.output_value.setObjectName("output_value")
        self.translate = QtWidgets.QPushButton(self.centralwidget)
        self.translate.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.translate.setObjectName("translate")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "输入词汇"))
        self.label_2.setText(_translate("MainWindow", "输出词汇"))
        self.translate.setText(_translate("MainWindow", "翻译"))


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec())

