# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browse_dialog.ui'
#
# Created: Wed Apr 27 09:52:41 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_BrowseDialog(object):
    def setupUi(self, BrowseDialog):
        BrowseDialog.setObjectName(_fromUtf8("BrowseDialog"))
        BrowseDialog.resize(530, 133)
        self.buttonBox = QtGui.QDialogButtonBox(BrowseDialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.browseButton = QtGui.QPushButton(BrowseDialog)
        self.browseButton.setGeometry(QtCore.QRect(420, 30, 87, 27))
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.urlEdit = QtGui.QLineEdit(BrowseDialog)
        self.urlEdit.setGeometry(QtCore.QRect(20, 30, 381, 27))
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))

        self.retranslateUi(BrowseDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BrowseDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BrowseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BrowseDialog)

    def retranslateUi(self, BrowseDialog):
        BrowseDialog.setWindowTitle(_translate("BrowseDialog", "Dialog", None))
        self.browseButton.setText(_translate("BrowseDialog", "Browse", None))

