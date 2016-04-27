#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals, print_function, absolute_import, division

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------

# pyqt
from PyQt4.QtGui import QDialog

from progress_dialog_ui import Ui_ProgressDialog


# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Progress(QDialog, Ui_ProgressDialog):

    # -------------------------------------------------------------------------
    # public methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        
  

