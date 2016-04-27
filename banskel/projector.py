#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division

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
    print(i)
    

# -----------------------------------------------------------------------------
def reproject(x, y, source_srid, dest_srid):
    
    sp = Proj("+init=EPSG:{}".format(source_srid))
    dp = Proj("+init=EPSG:{}".format(dest_srid))
    
    transform(sp,dp,x,y)

   

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
                reproject(tbl[7],tbl[6],"4326","21781")
            

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Projector(QThread):
    """
    TODO : declare signals
    """
    def __init__(self):
        super(Projector, self).__init__()
        self.filename = ""

    def filename(self, filename):
        self.filename = filename

    def run(self):
        # TODO
        #count_lines(self.filename)
        pass
