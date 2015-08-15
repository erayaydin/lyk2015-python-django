import os, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from layout import Ui_Dialog
import commands

class LampApp(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.apachebutton.clicked.connect(self.apacheToggle)
        self.ui.mysqlbutton.clicked.connect(self.mysqlToggle)
        #self.ui.pushButton.clicked.connect(self.CikisYap)
        if 'httpd' in commands.getoutput("ps -A"):
            print("Apache Running!")
        else:
            print("Apache not running!")

    def apacheToggle(self):
        print("apache!")

    def mysqlToggle(self):
        print("mysql!")

# Uygulama oluştur
app = QApplication(sys.argv)
lamp = LampApp()
lamp.show()
sys.exit(app.exec_())