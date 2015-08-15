import sys
# Import PyQt4 package (PyQt4 paketini ekle)
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# Create QT Application (QT uygulaması oluştur)
app = QApplication(sys.argv)

# Create base widget (Pencereyi oluştur)
widget = QWidget()

# Set window size (Pencere boyutunu ayarla)
widget.resize(320, 240)

# Set window title (Pencere başlığını belirle)
widget.setWindowTitle("Merhaba QT4")

# Add a button (Buton ekle)
btn = QPushButton("Çık", widget)

# Actions (işlemler)
@pyqtSlot()
def on_click():
	print("Butona tıklandı!")

@pyqtSlot()
def on_press():
	print("Butona basık tutuldu!")

@pyqtSlot()
def on_release():
	print('Butondan kalktı')

# Add tooltip to button (Buton üzerine gelince açıklama göster)
btn.setToolTip("Çıkmak için tıkla")
## Callbacks (Tetiklemeler)
# On Click Callback (Tıklanınca)
btn.clicked.connect(on_click)
# On Pressed Callback (Üzerine basılı tutunca)
btn.pressed.connect(on_press)
# On Released callback (Basılı tutarken kaldırınca)
btn.released.connect(on_release)
# Resize button (Butonu boyutlandır)
btn.resize(btn.sizeHint())
# Move button to 100x80 (Butonu 100x80 koordinatına taşı)
btn.move(100, 80)

# Show window (Pencereyi göster)
widget.show()

# Start app and exit from app (Uygulamayı başlat ve bitince çık)
sys.exit(app.exec())
