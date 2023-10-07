import typing
from PyQt5 import QtCore, QtWidgets
from untitledd import Ui_MainWindow
import sys
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QVBoxLayout,QMainWindow

class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myapp,self).__init__()

        self.benim=Ui_MainWindow()
        self.benim.setupUi(self)

        self.benim.cbkod.stateChanged.connect(self.showmeric)
        self.benim.cbsinema.stateChanged.connect(self.showmeric)
        self.benim.cbokul.stateChanged.connect(self.showmeric)
      
        self.benim.btnkydt.clicked.connect(self.getallcheckmeric)

    def getallcheckmeric(self):
        items=self.benim.centralwidget.findChildren(QtWidgets.QCheckBox)
        for meric in items:
            if meric.isChecked():
             
    def showmeric(self,value):
        meric=self.sender()
        print(meric.text())
        print(meric.isChecked())       

def app():
    mericap=QtWidgets.QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(mericap.exec_())   


app()