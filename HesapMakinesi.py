from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from HesapMakinesiA import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Number0.clicked.connect(self.push0)
        self.ui.Number1.clicked.connect(self.push1)
        self.ui.Number2.clicked.connect(self.push2)
        self.ui.Number3.clicked.connect(self.push3)
        self.ui.Number4.clicked.connect(self.push4)
        self.ui.Number5.clicked.connect(self.push5)
        self.ui.Number6.clicked.connect(self.push6)
        self.ui.Number7.clicked.connect(self.push7)
        self.ui.Number8.clicked.connect(self.push8)
        self.ui.Number9.clicked.connect(self.push9)
        self.ui.ButonTopla.clicked.connect(self.pusharti)
        self.ui.ButonCikar.clicked.connect(self.pusheksi)
        self.ui.ButonCarp.clicked.connect(self.pushcarpi)
        self.ui.ButonBol.clicked.connect(self.pushbol)
        self.ui.ButonSonuc.clicked.connect(self.PushSonuc)
        self.ui.ButonNokta.clicked.connect(self.PushNokta)
        self.ui.ButonTemizle.clicked.connect(self.PushTemizle)
        self.ui.ButonMod.clicked.connect(self.pushmod)
        

    def PushSonuc(self):
 
        equation = self.ui.EkranLabel.text()
 
        try:
            ans = eval(equation)
 
            self.ui.EkranLabel.setText(str(ans))
 
        except:
            self.ui.EkranLabel.setText("Wrong Input")


    def pusharti(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " + ")

    def pusheksi(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " - ")
    
    def pushcarpi(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " x ")

    def pushbol(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " ÷ ")
        
    def pushmod(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " % ")

    def PushNokta(self):
        text = self.ui.EkranLabel.text()
        self.ui.EkranLabel.setText(text + ".")


    def push0(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "0")

    def push1(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "1")

    def push2(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "2")

    def push3(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "3")

    def push4(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "4")

    def push5(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "5")

    def push6(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "6")

    def push7(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "7")

    def push8(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "8")

    def push9(self):
                sender = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(sender + "9")
    
    def PushTemizle(self):
        # clearing the label text
        self.ui.EkranLabel.setText("")

    
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()    
