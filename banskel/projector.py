#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals, print_function, absolute_import, division

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal

from pyproj import Proj, transform
import os
import io

# -----------------------------------------------------------------------------
# functions
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def count_lines(filename):
    i = 0
    with open(filename, "r+") as f:
        for line in f:
            i+=1
    return i-1
    

# -----------------------------------------------------------------------------
def reproject(x, y, source_srid, dest_srid):
    
    sp = Proj("+init=EPSG:{}".format(source_srid))
    dp = Proj("+init=EPSG:{}".format(dest_srid))
    
    return transform(sp,dp,x,y)

   

# -----------------------------------------------------------------------------
def transform_csv(filename, separator=','):
    i = 0
    with io.open(str(filename), "r+") as f:
        for line in f:
            if i == 0:
                i += 1
                pass
            else:
                tbl = line.split(separator)
                yield reproject(tbl[7],tbl[6],"4326","21781")
            

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Projector(QThread):
    progressSignal = pyqtSignal()
    finishSignal = pyqtSignal()
        
    def __init__(self):
        super(Projector, self).__init__()
        self.filename = ""

    def filename(self, filename):
        self.filename = filename

    def run(self):
        generator = transform_csv(self.filename)
        
        for result in generator:
            print(result)
            self.progressSignal.emit()
            
        self.finishSignal.emit()


