# -*- coding: utf-8 -*-
"""
Created on Thu May 30 22:17:52 2024

@author: monta
"""

from PyQt5 import uic

with open("projectui.py",'w', encoding="utf-8") as fout:
    uic.compileUi("project.ui", fout)