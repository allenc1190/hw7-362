import unittest
from leapyear import leapYear

class TestLeapYear(unittest.TestCase):

	def test_divisibleBy4(self):
		self.assertTrue(leapYear(2000))
		self.assertTrue(leapYear(2008))
		self.assertTrue(leapYear(2020))

	def test_divisibleBy100(self):
		self.assertFalse(leapYear(1700))
		self.assertFalse(leapYear(1900))
		self.assertFalse(leapYear(1800))
	
	def test_divisibleBy400(self):
		self.assertTrue(leapYear(2000))
		self.assertTrue(leapYear(2400))
		self.assertTrue(leapYear(2800))

if __name__ == '__main__':
	unittest.main()