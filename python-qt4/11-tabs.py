import sys
# Import PyQt4 package (PyQt4 paketini ekle)
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Create QT Application (QT uygulaması oluştur)
app  = QApplication(sys.argv)
tabs = QTabWidget()

# Create Tabs Widget (Tabları oluştur)
tab1 = QWidget()
tab2 = QWidget()
tab3 = QWidget()
tab4 = QWidget()

# Tabs Resize (Pencereyi yeniden boyutlandır)
tabs.resize(250, 150)

# Set layout for first tab (İlk tab için arayüz ayarla)
layout  = QVBoxLayout()
button1 = QPushButton("Başlat")
button2 = QPushButton("Ayarlar")
button3 = QPushButton("Durdur")
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
tab1.setLayout(layout)

# Add tabs (tabları ekle)
tabs.addTab(tab1, "Tab 1")
tabs.addTab(tab2, "Tab 2")
tabs.addTab(tab3, "Tab 3")
tabs.addTab(tab4, "Tab 4")

# Set title and show
tabs.setWindowTitle("Tab Örneği")
tabs.show()

# Start app and exit from app (Uygulamayı başlat ve bitince çık)
sys.exit(app.exec())
