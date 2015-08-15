import sys
# Import PyQt4 package (PyQt4 paketini ekle)
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Create QT Application (QT uygulaması oluştur)
app = QApplication(sys.argv)

# Table init
table = QTableWidget()
table.setWindowTitle("Tablo Örneği")
table.resize(400, 250)
table.setRowCount(4) # Satır sayısı
table.setColumnCount(2) # Sütun sayısı

# Set Headers (başlıklar)
table.setHorizontalHeaderLabels(str("Sütun1;Sütun2;").split(";"))
table.setVerticalHeaderLabels(str("Satır1;Satır2;Satır3;Satır4;").split(";"))

# Set Data (veriler)
table.setItem(0, 0, QTableWidgetItem("Öge (0,0)"))
table.setItem(0, 1, QTableWidgetItem("Öge (0,1)"))
table.setItem(1, 0, QTableWidgetItem("Öge (1,0)"))
table.setItem(1, 1, QTableWidgetItem("Öge (1,1)"))
table.setItem(2, 0, QTableWidgetItem("Öge (2,0)"))
table.setItem(2, 1, QTableWidgetItem("Öge (2,1)"))
table.setItem(3, 0, QTableWidgetItem("Öge (3,0)"))
table.setItem(3, 1, QTableWidgetItem("Öge (3,1)"))

# Cell Click (Satıra tıklama işlemi)
def cellClick(satir, sutun):
    print("Satır: " + str(satir) + ", Sutun: " + str(sutun))
table.cellClicked.connect(cellClick)

# Show table
table.show()

# Start app and exit from app (Uygulamayı başlat ve bitince çık)
sys.exit(app.exec())
