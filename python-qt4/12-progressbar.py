import sys
# Import PyQt4 package (PyQt4 paketini ekle)
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Create QT Application (QT uygulaması oluştur)
app  = QApplication(sys.argv)
widget = QWidget()
widget.resize(320, 240)
widget.setWindowTitle("Yükleme Bar Örneği")

# Create class for progressbar (Yükleme barı için sınıf oluşturalım)
class QProgBar(QProgressBar):
    value = 0

    @pyqtSlot()
    def increaseValue(progressbar):
        progressbar.setValue(progressbar.value)
        progressbar.value = progressbar.value+20

# Create progressBar (yükleme barını oluştur)
bar = QProgBar(widget)
bar.resize(300, 50)
bar.setValue(0)
bar.move(10, 20)

timer = QTimer()
bar.connect(timer, SIGNAL("timeout()"), bar, SLOT("increaseValue()"))
timer.start(400)

# Show the widget (Uygulamayı göster)
widget.show()

# Start app and exit from app (Uygulamayı başlat ve bitince çık)
sys.exit(app.exec())
