# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Deivison Barbosa\Desktop\projeto1\lista.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-50, -10, 871, 571))
        self.frame.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(260, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(70, 70, 771, 421))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.btnAlterarRegistro = QtWidgets.QPushButton(self.frame)
        self.btnAlterarRegistro.setGeometry(QtCore.QRect(90, 500, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnAlterarRegistro.setFont(font)
        self.btnAlterarRegistro.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btnAlterarRegistro.setObjectName("btnAlterarRegistro")
        self.btnDeletarRegistro = QtWidgets.QPushButton(self.frame)
        self.btnDeletarRegistro.setGeometry(QtCore.QRect(440, 500, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnDeletarRegistro.setFont(font)
        self.btnDeletarRegistro.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btnDeletarRegistro.setObjectName("btnDeletarRegistro")
        self.btnImprimir = QtWidgets.QPushButton(self.frame)
        self.btnImprimir.setGeometry(QtCore.QRect(680, 30, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnImprimir.setFont(font)
        self.btnImprimir.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btnImprimir.setObjectName("btnImprimir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Relat??rio de Produtos"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Produtos"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Pre??os"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Estoque"))
        self.btnAlterarRegistro.setText(_translate("MainWindow", "ALTERAR REGISTRO"))
        self.btnDeletarRegistro.setText(_translate("MainWindow", "DELETAR REGISTRO"))
        self.btnImprimir.setText(_translate("MainWindow", "IMPRIMIR"))
