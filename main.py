from PyQt5 import QtWidgets , QtGui,QtCore
from appui import Ui_MainWindow
import sys

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pgcd.clicked.connect(self.CalculatePGCD)
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.exit)
    
    def CalculatePGCD(self):
        self.statusbar.showMessage("")
        Num1 = int(self.first_num.text())
        Num2 = int(self.second_num.text())
        if Num1 > 0 and Num2 > 0:
            p = self.PGCD(Num1,Num2)
            self.textEdit.setText(self.textEdit.toPlainText()+"\n"+"le PGCD de "+str(Num1)+" et "+str(Num2)+" est "+str(p))
        else:
            self.statusbar.showMessage("Les nombres doivent être positifs !")

    def PGCD(self,Num1,Num2):
        self.textEdit.setText(self.textEdit.toPlainText()+"\nPGCD("+str(Num1)+","+str(Num2)+")")
        if Num1 > Num2:
            return self.PGCD(Num1-Num2,Num2)
        elif Num2 > Num1:
            return self.PGCD(Num1,Num2-Num1)
        else:
            return Num1

    def about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("PGCD:\nVersion:1.0\nProgrammer:Oussama Ben Sassi")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()                                                  

    def exit(self):
        QtWidgets.QApplication.quit() 




app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
sys.exit(app.exec_()) 
