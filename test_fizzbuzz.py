import unittest
from fizzbuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_returnSelf(self):
		self.assertEqual(fizzBuzz(7), 7)
		self.assertEqual(fizzBuzz(11), 11)
		self.assertEqual(fizzBuzz(19), 19)

	def test_returnFizz(self):
		self.assertEqual(fizzBuzz(6), "Fizz")
		self.assertEqual(fizzBuzz(9), "Fizz")

	def test_returnBuzz(self):
		self.assertEqual(fizzBuzz(25), "Buzz")
		self.assertEqual(fizzBuzz(35), "Buzz")
	
	def test_returnFizzBuzz(self):
		self.assertEqual(fizzBuzz(45), "FizzBuzz")
		self.assertEqual(fizzBuzz(90), "FizzBuzz")
		
if __name__ == '__main__':
	unittest.main()