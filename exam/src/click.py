# -*- coding: utf-8 -*-

# python2 vs python3
from sys import version_info
import compare
from tkinter import CENTER
if version_info.major == 2: #python2
		import Tkinter as tkinter
elif version_info.major == 3: #python3
		import tkinter as tkinter


def clicked():
           num1=txt.get()
           num2=txt2.get()
           def operating(num1, num2):
            if num1>num2:
             res = num1 + ">" + num2
            elif num1<num2:
             res = num1 + "<" + num2
            else:
             res = num1 + "=" + num2
            return res
           
           result = operating(num1, num2)
           tkinter.Label(window, text=result).grid(row=3)
           
            
    