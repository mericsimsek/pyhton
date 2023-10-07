from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon  



def window():

    app=QApplication(sys.argv)
    win=QMainWindow()


    def clicked(self):
     print('Im meric, logined hehehe:) Your name :  '+txt_name.text()+'  Your surname :'+txt_surname.text())


    win.setWindowTitle("Meric app")#isim yazdırır
    win.setGeometry(300,300,700,700)#uyg. boyutunu yazdırır
    win.setWindowIcon(QIcon('mericme.jpg'))
    win.setToolTip("my tools meric")

    lbl_name=QtWidgets.QLabel(win)
    lbl_name.setText("Name:")
    lbl_name.move(50,30)

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText("Surname:") #cout 
    lbl_surname.move(50,60)#y de biraz daha aşağısında olacak 

    txt_name=QtWidgets.QLineEdit(win)#cin
    txt_name.move(103,30)#kutucuk ekleyecez your namenin x kordinantta da biraz daha sağa ekleyececez bu yüzden 100 yazdım

    txt_surname=QtWidgets.QLineEdit(win)#cin
    txt_surname.move(123,60)

    buttonn=QtWidgets.QPushButton(win)#tıklanacak buton
    buttonn.setText('Login hehehe')
    buttonn.move(190,90)
    buttonn.clicked.connect(clicked)#click için bi fonksiyon yazacaz şimdi

    win.show()

    sys.exit(app.exec_())

window()