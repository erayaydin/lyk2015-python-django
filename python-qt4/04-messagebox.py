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

# Add QuestionBox button (Soru kutusu için buton ekle)
qb_btn = QPushButton("Mesaj Kutusu", widget)

# Actions (işlemler)
@pyqtSlot()
def qb_show():
	# Create message box and return result (Mesaj kutusu oluştur ve kullanıcının cevabını değişkene aktar)
	cevap = QMessageBox.question(widget, 'Mesaj', 'Soru', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
	
	# If user click to Yes button (Eğer kullanıcı 'Evet' cevabı döndürürse)
	if cevap == QMessageBox.Yes:
		sys.exit()

# Add tooltip to button (Buton üzerine gelince açıklama göster)
qb_btn.setToolTip("Soru mesaj kutusu oluşturmak için tıklayınız")
## Callbacks (Tetiklemeler)
# On Click Callback (Tıklanınca)
btn.clicked.connect(qb_show)
# Resize button (Butonu boyutlandır)
btn.resize(btn.sizeHint())
# Move button to 100x80 (Butonu 100x80 koordinatına taşı)
btn.move(100, 80)

# Show window (Pencereyi göster)
widget.show()

# Start app and exit from app (Uygulamayı başlat ve bitince çık)
sys.exit(app.exec())
