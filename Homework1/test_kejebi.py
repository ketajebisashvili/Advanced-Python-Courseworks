import unittest
from src import traingle_kejebi

class TestArea(unittest.TestCase):
    def  test_area_traingle1(self):
        self.assertEquals(traingle_kejebi.area_calculator(4, 5), 10.00, "should return 10.00" )
    def  test_area_traingle2(self):
        self.assertEquals(traingle_kejebi.area_calculator(4, 7), 14.00, "should return 14.00" )
    def  test_area_traingle3(self):
        self.assertEquals(traingle_kejebi.area_calculator(5, 7), 17.50, "should return 17.50" )

