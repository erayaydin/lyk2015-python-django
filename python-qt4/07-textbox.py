import sys
# Import PyQt4 package (PyQt4 paketini ekle)
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# Create QT Application (QT uygulaması oluştur)
app = QApplication(sys.argv)

# Create base window (Pencereyi oluştur)
widget = QMainWindow()

# Set window size (Pencere boyutunu ayarla)
widget.resize(320, 240)

# Set window title (Pencere başlığını belirle)
widget.setWindowTitle("Merhaba QT4")

# Create textbox (yazı alanı oluştur)
textbox = QLineEdit(widget)
textbox.move(30, 30)
textbox.resize(260, 20)

# Show window (Pencereyi göster)
widget.show()

# Start app and exit from app (Uygulamayı başlat ve bitince çık)
sys.exit(app.exec())
