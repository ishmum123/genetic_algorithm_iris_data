from unittest import TestCase
from inspect import signature
from sys import path
from os.path import dirname, join

path.append(join(dirname(__file__), ".."))

from function_generator import FunctionGenerator


class TestFunctionGenerator(TestCase):
	def setUp(self):
		self.generator = FunctionGenerator()

	def getFunctionLength(self, function):
		return len(signature(function).parameters)

	def test_getFunction_returns_function_taking_two_arguments(self):
		test_func = self.generator.getFunction
		self.assertTrue(callable(test_func(1, 1)))
		self.assertEqual(self.getFunctionLength(test_func), 2)

	def test_getFunction_returns_1_argument_function_given_1(self):
		test_func = self.generator.getFunction(1, 0)
		self.assertEqual(self.getFunctionLength(test_func), 1)

	def test_getFunction_returns_2_argument_function_given_2(self):
		test_func = self.generator.getFunction(2, 0)
		self.assertEqual(self.getFunctionLength(test_func), 2)

	def test_getFunction_raises_ValuEerror_if_not_supplied_with_1_or_2(self):
		test_func = self.generator.getFunction
		with self.assertRaises(ValueError):
			test_func(0, 0)
		with self.assertRaises(ValueError):
			test_func(3, 0)
		with self.assertRaises(ValueError):
			test_func("anything", 0)

	def test_getFunction_returns_different_functions_for_some_func_num(self):
		test_func = self.generator.getFunction
		self.assertNotEqual(test_func(1, 0)(0), test_func(1, 1)(0))
		self.assertNotEqual(test_func(2, 0)(0, 1), test_func(2, 1)(0, 1))
