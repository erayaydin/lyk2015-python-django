import os, sys
# Import PyQt4 package (PyQt4 paketini ekle)
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# form.py dosyasından Ui_Dialog'u ekle
from form import Ui_Dialog

class MyApp(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # UI olarak form.py'deki Ui_Dialog'u kullan
        self.ui = Ui_Dialog()
        # UI'yi oluştur
        self.ui.setupUi(self)
        # Butona tıklanırsa tetikle
        self.ui.pushButton.clicked.connect(self.CikisYap)

    def CikisYap(self):
        sys.exit()

# Uygulama oluştur
app = QApplication(sys.argv)
myapp = MyApp()
myapp.show()
sys.exit(app.exec_())