from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon  

class mywindow(QMainWindow):
 def __init__(self):
    super(mywindow,self).__init__()

    self.setWindowTitle("Meric app")#isim yazdırır
    self.setGeometry(300,300,700,700)#uyg. boyutunu yazdırır
    self.setWindowIcon(QIcon('mericme.jpg'))
    self.setToolTip("my tools meric")
    self.initUI()

 def initUI(self):
    self.lbl_name=QtWidgets.QLabel(self)
    self.lbl_name.setText("Name:")
    self.lbl_name.move(50,30)
    
    self.lbl_surname=QtWidgets.QLabel(self)
    self.lbl_surname.setText("Surname:") #cout 
    self.lbl_surname.move(50,60)#y de biraz daha aşağısında olacak 

    self.txt_name=QtWidgets.QLineEdit(self)#cin
    self.txt_name.move(103,30)#kutucuk ekleyecez your namenin x kordinantta da biraz daha sağa ekleyececez bu yüzden 100 yazdım
    

    self.txt_surname=QtWidgets.QLineEdit(self)#cin
    self.txt_surname.move(123,60)
    
    self.lbl_result=QtWidgets.QLabel(self)#burayı yapmamızın sebebi giriş yapılınca logined hehe yazısınını yazdırmak bunu def clickede taşıyacaz
    self.lbl_result.resize(500,50)#bu nasıl your surname yazıca sadece your surn kısmına kadar yazdırdıysa sığmadıysa aşağıdaki ım meric logined hehe yazısını sığdırmak için 300 karakter boşluk açtk
    self.lbl_result.move(150,150)

    self.buttonn=QtWidgets.QPushButton(self)#tıklanacak buton
    self.buttonn.setText('Login hehehe')
    self.buttonn.move(190,90)
    self.buttonn.clicked.connect(self.clicked)#click için bi fonksiyon yazacaz şimdi

 def clicked(self):
     self.lbl_result.setText('Im meric, logined hehehe:) Your name :  '+self.txt_name.text()+'  Your surname :'+self.txt_surname.text())

def window():
    app=QApplication(sys.argv)
    win=mywindow()

    win.show()

    sys.exit(app.exec_())


window()