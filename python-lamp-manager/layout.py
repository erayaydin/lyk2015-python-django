# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(239, 65)
        self.mysqlbutton = QtGui.QPushButton(Dialog)
        self.mysqlbutton.setGeometry(QtCore.QRect(10, 10, 101, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../home/eray/Desktop/mysql.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mysqlbutton.setIcon(icon)
        self.mysqlbutton.setIconSize(QtCore.QSize(32, 32))
        self.mysqlbutton.setObjectName(_fromUtf8("mysqlbutton"))
        self.apachebutton = QtGui.QPushButton(Dialog)
        self.apachebutton.setGeometry(QtCore.QRect(120, 10, 101, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../home/eray/Desktop/apache.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apachebutton.setIcon(icon1)
        self.apachebutton.setIconSize(QtCore.QSize(32, 32))
        self.apachebutton.setObjectName(_fromUtf8("apachebutton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "LAMP Manager", None))
        self.mysqlbutton.setText(_translate("Dialog", "MySQL", None))
        self.apachebutton.setText(_translate("Dialog", "Apache", None))

