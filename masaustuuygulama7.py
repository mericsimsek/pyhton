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

        self.benim.tr.toggled.connect(self.onclicked)
        self.benim.abd.toggled.connect(self.onclicked)
        self.benim.grmn.toggled.connect(self.onclicked)
        self.benim.fra.toggled.connect(self.onclicked)
    def onclicked(self):
        rb=self.sender()
        if rb.isChecked():
            print('chanced radio is:'+rb.text())

        self.benim.lise.toggled.connect(self.onclickedduzey)
        self.benim.sfw.toggled.connect(self.onclickedduzey)
        self.benim.ni.toggled.connect(self.onclickedduzey)
        self.benim.fra.toggled.connect(self.onclickedduzey)


    def onclickedduzey(self):
        rb=self.sender()
        if rb.isChecked():
            print('Level is:'+rb.text())


        self.benim.pushbtn.clicked.connect(self.getselectulke)
        self.benim.pushbtn2.clicked.connect(self.getselectlevel)

    def getselectulke(self):
        items=self.benim.groupboxulke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.benim.lblulke.setText('secilen ulke:'+rb.text())

    def getselectlevel(self):
        items=self.benim.groupboxlevel.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.benim.lbl2.setText('secilen duzey:'+rb.text())
def myapp():
    app=QtWidgets.QApplication(sys.argv)
    win=mywindow()
    win.show()
    sys.exit(app.exec_())

myapp()
