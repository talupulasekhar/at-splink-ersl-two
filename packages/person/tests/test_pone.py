import unittest
# Import the functions you want to test
#from person.pone import printHello
from packages.person.src.person.pone import printHello

class TestPone(unittest.TestCase):
    def test_print_hello(self):
        self.assertEqual(printHello(),"hello")


