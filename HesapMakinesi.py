from PyQt5 import QtWidgets
from HesapMakinesiA import Ui_HesapMakinesi
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_HesapMakinesi()
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
        Denklem = self.ui.EkranLabel.text()
 
        try:
            Cevap = eval(Denklem)
 
            self.ui.EkranLabel.setText(str(Cevap))
 
        except:
            self.ui.EkranLabel.setText("Hatalı Giriş")


    def pusharti(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " + ")

    def pusheksi(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " - ")
    
    def pushcarpi(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " * ")

    def pushbol(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " / ")
        
    def pushmod(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + " % ")

    def PushNokta(self):
        text = self.ui.EkranLabel.text()
        self.ui.EkranLabel.setText(text + ".")


    def push0(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "0")

    def push1(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "1")

    def push2(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "2")

    def push3(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "3")

    def push4(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "4")

    def push5(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "5")

    def push6(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "6")

    def push7(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "7")

    def push8(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "8")

    def push9(self):
                text = self.ui.EkranLabel.text()
                self.ui.EkranLabel.setText(text + "9")
    
    def PushTemizle(self):
        # clearing the label text
        self.ui.EkranLabel.setText("")

    
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()    
