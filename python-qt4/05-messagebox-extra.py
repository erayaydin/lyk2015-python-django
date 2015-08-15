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

# Actions (işlemler)
@pyqtSlot()
def qb_show():
	# Create message box and return result (Mesaj kutusu oluştur ve kullanıcının cevabını değişkene aktar)
	cevap = QMessageBox.question(widget, 'Mesaj', 'Soru', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
	
	# If user click to Yes button (Eğer kullanıcı 'Evet' cevabı döndürürse)
	if cevap == QMessageBox.Yes:
		print("[Question Box] YES!")
	else:
		print("[Question Box] NO!")

@pyqtSlot()
def wb_show():
	QMessageBox.warning(widget, 'Mesaj', 'Uyarı')

@pyqtSlot()
def ib_show():
	QMessageBox.information(widget, 'Mesaj', 'Bilgi mesajı')

@pyqtSlot()
def cb_show():
	QMessageBox.critical(widget, 'Mesaj', 'Kritik hata mesajı')

@pyqtSlot()
def ab_show():
	QMessageBox.about(widget, 'Mesaj', 'Basit bilgi mesajı')

# Question Box Button (Soru Kutusu için buton)
qb_btn = QPushButton("Soru Kutusu", widget)
qb_btn.setToolTip("Soru mesaj kutusu oluşturmak için tıklayınız")
qb_btn.clicked.connect(qb_show)
qb_btn.resize(qb_btn.sizeHint())
qb_btn.move(30, 30)

# Warning Box Button (Uyarı kutusu için buton)
wb_btn = QPushButton("Uyarı Kutusu", widget)
wb_btn.setToolTip("Uyarı mesaj kutusu oluşturmak için tıklayınız")
wb_btn.clicked.connect(wb_show)
wb_btn.resize(wb_btn.sizeHint())
wb_btn.move(120, 30)

# Information Box Button (Bilgi kutusu için buton)
ib_btn = QPushButton("Bilgi Kutusu", widget)
ib_btn.setToolTip("Bilgi mesaj kutusu oluşturmak için tıklayınız")
ib_btn.clicked.connect(ib_show)
ib_btn.resize(ib_btn.sizeHint())
ib_btn.move(210, 30)

# Critical Box Button (Kritik mesaj kutusu için buton)
cb_btn = QPushButton("Kritik Hata", widget)
cb_btn.setToolTip("Kritik hata mesaj kutusu oluşturmak için tıklayınız")
cb_btn.clicked.connect(cb_show)
cb_btn.resize(cb_btn.sizeHint())
cb_btn.move(30, 60)

# About Box Button (Basit mesaj kutusu için buton)
ab_btn = QPushButton("Basit Mesaj", widget)
ab_btn.setToolTip("Basit mesaj kutusu oluşturmak için tıklayınız")
ab_btn.clicked.connect(ab_show)
ab_btn.resize(ab_btn.sizeHint())
ab_btn.move(120, 60)

# Show window (Pencereyi göster)
widget.show()

# Start app and exit from app (Uygulamayı başlat ve bitince çık)
sys.exit(app.exec())
