# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Admin\Desktop\Programação\VS Code\4. Python\QTprojetos\Duas telas\tela2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 372)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(120, 120, 120);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(184, 272, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Admin\\Desktop\\Programação\\VS Code\\4. Python\\QTprojetos\\Duas telas\\Imagens/Adicionar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.nome = QtWidgets.QLineEdit(self.centralwidget)
        self.nome.setGeometry(QtCore.QRect(140, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nome.setFont(font)
        self.nome.setStyleSheet("color: rgb(81, 81, 81);")
        self.nome.setObjectName("nome")
        self.datdia = QtWidgets.QLineEdit(self.centralwidget)
        self.datdia.setGeometry(QtCore.QRect(140, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.datdia.setFont(font)
        self.datdia.setStyleSheet("color: rgb(81, 81, 81);")
        self.datdia.setObjectName("datdia")
        self.debitoreal = QtWidgets.QLineEdit(self.centralwidget)
        self.debitoreal.setGeometry(QtCore.QRect(140, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.debitoreal.setFont(font)
        self.debitoreal.setStyleSheet("color: rgb(81, 81, 81);")
        self.debitoreal.setObjectName("debitoreal")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(120, 120, 120);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(120, 120, 120);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(120, 120, 120);")
        self.label_4.setObjectName("label_4")
        self.datmes = QtWidgets.QLineEdit(self.centralwidget)
        self.datmes.setGeometry(QtCore.QRect(210, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.datmes.setFont(font)
        self.datmes.setStyleSheet("color: rgb(81, 81, 81);")
        self.datmes.setObjectName("datmes")
        self.datano = QtWidgets.QLineEdit(self.centralwidget)
        self.datano.setGeometry(QtCore.QRect(280, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.datano.setFont(font)
        self.datano.setStyleSheet("color: rgb(81, 81, 81);")
        self.datano.setObjectName("datano")
        self.debitocentavos = QtWidgets.QLineEdit(self.centralwidget)
        self.debitocentavos.setGeometry(QtCore.QRect(280, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.debitocentavos.setFont(font)
        self.debitocentavos.setStyleSheet("color: rgb(81, 81, 81);")
        self.debitocentavos.setObjectName("debitocentavos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 19))
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
        self.label.setText(_translate("MainWindow", "CADASTRO"))
        self.pushButton.setText(_translate("MainWindow", " Cadastrar"))
        self.label_2.setText(_translate("MainWindow", "NOME"))
        self.label_3.setText(_translate("MainWindow", "DATA"))
        self.label_4.setText(_translate("MainWindow", "DÉBITO"))
