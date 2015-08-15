import os, sys
# Import PyQt4 package (PyQt4 paketini ekle)
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Create QT Application (QT uygulaması oluştur)
app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle("Resim örneği")

# Create widget (Bileşen oluştur)
label  = QLabel(widget)
pixmap = QPixmap(os.getcwd() + "/python.png")
label.setPixmap(pixmap)
widget.resize(pixmap.width(), pixmap.height())

# Show widget (Bileşeni göster)
widget.show()

# Start app and exit from app (Uygulamayı başlat ve bitince çık)
sys.exit(app.exec())
