# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HesapMakinesi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HesapMakinesi(object):
    def setupUi(self, HesapMakinesi):
        HesapMakinesi.setObjectName("HesapMakinesi")
        HesapMakinesi.setEnabled(True)
        HesapMakinesi.resize(485, 360)
        HesapMakinesi.setFocusPolicy(QtCore.Qt.NoFocus)
        HesapMakinesi.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HesapMakinesi.setWindowIcon(icon)
        HesapMakinesi.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        HesapMakinesi.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(HesapMakinesi)
        self.centralwidget.setObjectName("centralwidget")
        self.ButonSonuc = QtWidgets.QPushButton(self.centralwidget)
        self.ButonSonuc.setGeometry(QtCore.QRect(380, 90, 62, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButonSonuc.setFont(font)
        self.ButonSonuc.setStyleSheet("background: #bdbebd;")
        self.ButonSonuc.setObjectName("ButonSonuc")
        self.ButonBol = QtWidgets.QPushButton(self.centralwidget)
        self.ButonBol.setGeometry(QtCore.QRect(280, 90, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButonBol.setFont(font)
        self.ButonBol.setStyleSheet("background: #bdbebd;")
        self.ButonBol.setObjectName("ButonBol")
        self.ButonTopla = QtWidgets.QPushButton(self.centralwidget)
        self.ButonTopla.setGeometry(QtCore.QRect(280, 270, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButonTopla.setFont(font)
        self.ButonTopla.setStyleSheet("background: #bdbebd;")
        self.ButonTopla.setObjectName("ButonTopla")
        self.ButonCarp = QtWidgets.QPushButton(self.centralwidget)
        self.ButonCarp.setGeometry(QtCore.QRect(280, 150, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButonCarp.setFont(font)
        self.ButonCarp.setStyleSheet("background: #bdbebd;")
        self.ButonCarp.setObjectName("ButonCarp")
        self.ButonCikar = QtWidgets.QPushButton(self.centralwidget)
        self.ButonCikar.setGeometry(QtCore.QRect(280, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButonCikar.setFont(font)
        self.ButonCikar.setStyleSheet("background: #bdbebd;")
        self.ButonCikar.setObjectName("ButonCikar")
        self.Number7 = QtWidgets.QPushButton(self.centralwidget)
        self.Number7.setGeometry(QtCore.QRect(40, 90, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number7.setFont(font)
        self.Number7.setStyleSheet("background: #bdbebd;")
        self.Number7.setObjectName("Number7")
        self.Number4 = QtWidgets.QPushButton(self.centralwidget)
        self.Number4.setGeometry(QtCore.QRect(40, 150, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number4.setFont(font)
        self.Number4.setStyleSheet("background: #bdbebd;")
        self.Number4.setObjectName("Number4")
        self.Number1 = QtWidgets.QPushButton(self.centralwidget)
        self.Number1.setGeometry(QtCore.QRect(40, 210, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number1.setFont(font)
        self.Number1.setStyleSheet("background: #bdbebd;")
        self.Number1.setObjectName("Number1")
        self.Number8 = QtWidgets.QPushButton(self.centralwidget)
        self.Number8.setGeometry(QtCore.QRect(120, 90, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number8.setFont(font)
        self.Number8.setStyleSheet("background: #bdbebd;")
        self.Number8.setObjectName("Number8")
        self.Number5 = QtWidgets.QPushButton(self.centralwidget)
        self.Number5.setGeometry(QtCore.QRect(120, 150, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number5.setFont(font)
        self.Number5.setStyleSheet("background: #bdbebd;")
        self.Number5.setObjectName("Number5")
        self.Number2 = QtWidgets.QPushButton(self.centralwidget)
        self.Number2.setGeometry(QtCore.QRect(120, 210, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number2.setFont(font)
        self.Number2.setStyleSheet("background: #bdbebd;")
        self.Number2.setObjectName("Number2")
        self.Number3 = QtWidgets.QPushButton(self.centralwidget)
        self.Number3.setGeometry(QtCore.QRect(200, 210, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number3.setFont(font)
        self.Number3.setStyleSheet("background: #bdbebd;")
        self.Number3.setObjectName("Number3")
        self.Number6 = QtWidgets.QPushButton(self.centralwidget)
        self.Number6.setGeometry(QtCore.QRect(200, 150, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number6.setFont(font)
        self.Number6.setStyleSheet("background: #bdbebd;")
        self.Number6.setObjectName("Number6")
        self.Number9 = QtWidgets.QPushButton(self.centralwidget)
        self.Number9.setGeometry(QtCore.QRect(200, 90, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number9.setFont(font)
        self.Number9.setStyleSheet("background: #bdbebd;")
        self.Number9.setObjectName("Number9")
        self.Number0 = QtWidgets.QPushButton(self.centralwidget)
        self.Number0.setGeometry(QtCore.QRect(40, 270, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Number0.setFont(font)
        self.Number0.setStyleSheet("background: #bdbebd;")
        self.Number0.setObjectName("Number0")
        self.ButonNokta = QtWidgets.QPushButton(self.centralwidget)
        self.ButonNokta.setGeometry(QtCore.QRect(120, 270, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButonNokta.setFont(font)
        self.ButonNokta.setStyleSheet("background: #bdbebd;")
        self.ButonNokta.setObjectName("ButonNokta")
        self.ButonTemizle = QtWidgets.QPushButton(self.centralwidget)
        self.ButonTemizle.setGeometry(QtCore.QRect(380, 210, 62, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButonTemizle.setFont(font)
        self.ButonTemizle.setStyleSheet("background: #bdbebd;")
        self.ButonTemizle.setObjectName("ButonTemizle")
        self.ButonMod = QtWidgets.QPushButton(self.centralwidget)
        self.ButonMod.setGeometry(QtCore.QRect(200, 270, 62, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ButonMod.setFont(font)
        self.ButonMod.setStyleSheet("background: #bdbebd;")
        self.ButonMod.setObjectName("ButonMod")
        self.EkranLabel = QtWidgets.QLabel(self.centralwidget)
        self.EkranLabel.setGeometry(QtCore.QRect(40, 20, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.EkranLabel.setFont(font)
        self.EkranLabel.setAutoFillBackground(False)
        self.EkranLabel.setStyleSheet("border : 5px solid #fffff1; background : #fffff1;")
        self.EkranLabel.setText("")
        self.EkranLabel.setWordWrap(True)
        self.EkranLabel.setObjectName("EkranLabel")
        HesapMakinesi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HesapMakinesi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        HesapMakinesi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HesapMakinesi)
        self.statusbar.setObjectName("statusbar")
        HesapMakinesi.setStatusBar(self.statusbar)

        self.retranslateUi(HesapMakinesi)
        QtCore.QMetaObject.connectSlotsByName(HesapMakinesi)

    def retranslateUi(self, HesapMakinesi):
        _translate = QtCore.QCoreApplication.translate
        HesapMakinesi.setWindowTitle(_translate("HesapMakinesi", "HesapMakinesi"))
        self.ButonSonuc.setText(_translate("HesapMakinesi", "Sonuç"))
        self.ButonBol.setText(_translate("HesapMakinesi", "÷"))
        self.ButonTopla.setText(_translate("HesapMakinesi", "+"))
        self.ButonCarp.setText(_translate("HesapMakinesi", "×"))
        self.ButonCikar.setText(_translate("HesapMakinesi", "-"))
        self.Number7.setText(_translate("HesapMakinesi", "7"))
        self.Number4.setText(_translate("HesapMakinesi", "4"))
        self.Number1.setText(_translate("HesapMakinesi", "1"))
        self.Number8.setText(_translate("HesapMakinesi", "8"))
        self.Number5.setText(_translate("HesapMakinesi", "5"))
        self.Number2.setText(_translate("HesapMakinesi", "2"))
        self.Number3.setText(_translate("HesapMakinesi", "3"))
        self.Number6.setText(_translate("HesapMakinesi", "6"))
        self.Number9.setText(_translate("HesapMakinesi", "9"))
        self.Number0.setText(_translate("HesapMakinesi", "0"))
        self.ButonNokta.setText(_translate("HesapMakinesi", "."))
        self.ButonTemizle.setText(_translate("HesapMakinesi", "Temizle"))
        self.ButonMod.setText(_translate("HesapMakinesi", "%"))
