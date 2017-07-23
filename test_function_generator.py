from unittest import TestCase
from function_generator import FunctionGenerator


class TestFunctionGenerator(TestCase):
	def setUp(self):
		self.generator = FunctionGenerator()

	def test_getFunction_returns_function(self):
		self.assertTrue(callable(self.generator.getFunction(1)))

	def test_getFunction_returns_1_argument_function_given_1(self):
		test_func = self.generator.getFunction(1)
		with self.assertRaises(Exception):
			test_func()
		with self.assertRaises(Exception):
			test_func(0, 0)
		test_func(0)

	def test_getFunction_returns_2_argument_function_given_2(self):
		test_func = self.generator.getFunction(2)
		with self.assertRaises(TypeError):
			test_func()
		with self.assertRaises(TypeError):
			test_func(0)
		test_func(0, 0)

	def test_getFunction_raises_ValuEerror_if_not_supplied_with_1_or_2(self):
		with self.assertRaises(ValueError):
			self.generator.getFunction(0)
		with self.assertRaises(ValueError):
			self.generator.getFunction(3)
		with self.assertRaises(Exception):
			self.generator.getFunction("anything")
