from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from HesapMakinesiA import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Number0.clicked.connect(self.PushButton)
        self.ui.Number1.clicked.connect(self.PushButton)
        self.ui.Number2.clicked.connect(self.PushButton)
        self.ui.Number3.clicked.connect(self.PushButton)
        self.ui.Number4.clicked.connect(self.PushButton)
        self.ui.Number5.clicked.connect(self.PushButton)
        self.ui.Number6.clicked.connect(self.PushButton)
        self.ui.Number7.clicked.connect(self.PushButton)
        self.ui.Number8.clicked.connect(self.PushButton)
        self.ui.Number9.clicked.connect(self.PushButton)
        self.ui.ButonBol.clicked.connect(self.PushButton)
        self.ui.ButonCarp.clicked.connect(self.PushButton)
        self.ui.ButonCikar.clicked.connect(self.PushButton)
        self.ui.ButonTopla.clicked.connect(self.PushButton)
        self.ui.ButonMod.clicked.connect(self.PushButton)
        self.ui.ButonNokta.clicked.connect(self.PushButton)

        




    def PushButton(self,value):
        sender = self.sender().text()

        self.ui.Ekran.setText(sender)


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()    
