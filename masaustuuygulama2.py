import typing
from PyQt5 import QtCore, QtWidgets

import sys
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QVBoxLayout,QMainWindow


class mycolor(QWidget):
    def __init__(self,renk):
        super(mycolor,self).__init__()
        self.setAutoFillBackground(True)#true yapınca arkaplanı otomatik boyuyor

        mypalette=self.palette()#palet boya işlemini yapar
        mypalette.setColor(QPalette.Window,QColor(renk))
        self.setPalette(mypalette)



class mywindow(QMainWindow):#bunların çalışması için bir window gerek her zaman
    def __init__(self):
        super(mywindow,self).__init__()
        self.setGeometry(200,200,500,500)

        hmylay=QtWidgets.QVBoxLayout()
        hmylay.addWidget(mycolor('blue'))
        hmylay.addWidget(mycolor('black'))
        hmylay.addWidget(mycolor('red'))

        hmylay2=QtWidgets.QVBoxLayout()
        hmylay2.addWidget(mycolor('yellow'))
        hmylay2.addWidget(mycolor('green'))

        vlay=QtWidgets.QHBoxLayout()
        vlay.addLayout(hmylay)
        vlay.addLayout(hmylay2)
        mywidget=QWidget()
        mywidget.setLayout(vlay)

        self.setCentralWidget(mywidget)


def app():
    app=QApplication(sys.argv)
    win=mywindow()
    win.show()
    sys.exit(app.exec_())

app()