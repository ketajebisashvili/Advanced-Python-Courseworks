import unittest
import sys, os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import compare
del sys.path[0]

from sys import version_info
if version_info.major == 2: #python2
		import Tkinter as tkinter
elif version_info.major == 3: #python3
		import tkinter as tkinter


class Test(unittest.TestCase):
    
    def testLess(self):
        self.assertEqual(compare.operating(3,5), (3, '<', 5))
    def testGreater(self):
         self.assertEqual(compare.operating(4,0), (4, '>', 0))
    def testEqual(self):
        self.assertEqual(compare.operating(6,6), (6, '=', 6))

        