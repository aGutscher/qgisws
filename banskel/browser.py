#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division


# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
# standard
import os

# pyqt
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QDialogButtonBox
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import QDir
from PyQt4.QtCore import pyqtSignal

from browse_dialog_ui import Ui_BrowseDialog
from projector import Projector, count_lines
from progressbar import Progress

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Browser(QDialog, Ui_BrowseDialog):

    # -------------------------------------------------------------------------
    # public methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self, app):
        QDialog.__init__(self)
        self.setupUi(self)
        self.app = app
        # init attributes
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        self.filename = "/home/vagrant/Bureau/fork/qgisws/banskel/bano-75.csv"
        
        self.browseButton.clicked.connect(self.__browse)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.__ok)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(app.quit)

        self.projector = Projector()
        self.progress = Progress()

    # -------------------------------------------------------------------------
    @property
    def filename(self):
        return self.__filename

    # -------------------------------------------------------------------------
    @filename.setter
    def filename(self, filename):
        if os.path.isfile(filename):
            self.__filename = filename
            self.urlEdit.setText(self.__filename)
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False) 
            msg = QMessageBox()
            msg.setText("Fichier introuvable")

    # -------------------------------------------------------------------------
    # private methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __in_progress(self):
        self.progress.progressBar.setValue(self.progress.progressBar.value()+1)

    # -------------------------------------------------------------------------
    def __compute_done(self):
        self.progress.close()

    # -------------------------------------------------------------------------
    def __ok(self):
        self.projector.filename = self.__filename
        
        self.projector.progressSignal.connect(self.__in_progress)
        self.projector.finishSignal.connect(self.__compute_done)
        self.projector.start()
        
        self.progress.progressBar.setRange(0,count_lines(self.__filename))
        self.progress.progressBar.setValue(0)
        self.progress.show()


    # -------------------------------------------------------------------------
    def __browse(self):
        self.filename = QFileDialog.getOpenFileName(self,"Sélectionner le fichier")
        
