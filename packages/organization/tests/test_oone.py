import unittest
# Import the functions you want to test
#from organization.oone import printPolo
from packages.organization.src.organization.oone import printPolo

class test_print_polo(unittest.TestCase):
    def test_print_hello(self):
        self.assertEqual(printPolo(),"polo")


