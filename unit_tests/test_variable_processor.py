from unittest import TestCase
from sys import path
from os.path import dirname, join

path.append(join(dirname(__file__), ".."))

from variable_processor import VariableProcessor


class TestVariableProcessor(TestCase):
	def setUp(self):
		self.processor = VariableProcessor()

	def test_getFunctions_returns_list_of_n_functions(self):
		test_func = self.processor.getFunctions
		self.assertTrue(isinstance(test_func(0), list))
		for i in range(1, 5):
			self.assertEqual(len(test_func(i)), i)
			self.assertTrue(callable(test_func(i)[i - 1]))

	def test_getFunctions_does_not_always_return_same_function(self):
		test_func = self.processor.getFunctions
		num_func = 50
		returns_same_func = True
		func_list = test_func(num_func)
		for i in range(1, len(func_list)):
			try:
				if func_list[i](0) != func_list[i - 1](0):
					returns_same_func = False
			except Exception:
				pass
		self.assertFalse(returns_same_func)
