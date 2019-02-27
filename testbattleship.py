import unittest
from battleship import *
class TestBattleship(unittest.TestCase):
	def test_hello(self):
		self.assertEqual(hello_world(), 'hello world')