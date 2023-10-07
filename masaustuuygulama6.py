import typing
from PyQt5 import QtCore, QtWidgets
from untitledd import Ui_MainWindow
import sys
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QVBoxLayout,QMainWindow


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.benim=Ui_MainWindow()
        self.benim.setupUi(self)
       
        
        self.benim.btnitemyukle.clicked.connect(self.loaditem)
        self.benim.btnitemgetir.clicked.connect(self.getitem)
        self.benim.comboboxmeric.currentIndexChanged.connect(self.deleted)
        self.benim.comboboxmeric.currentIndexChanged[str].connect(self.textt)
        self.benim.btnitemclear.clicked.connect(self.clearitem)
    def clearitem(self):
        self.benim.comboboxmeric.clear()
    def deleted(self,index):
        print(index)

    def textt(self,text):
        print(text)


    def loaditem(self):
        sehirler=['Bursa','Eskişehir','Boston','Chicago']
        self.benim.comboboxmeric.addItems(sehirler)

    def getitem(self):
        print(self.benim.comboboxmeric.currentIndex())
        print(self.benim.comboboxmeric.currentText())

def myapp():
    app=QtWidgets.QApplication(sys.argv)
    win=mywindow()
    win.show()
    sys.exit(app.exec_())

myapp()