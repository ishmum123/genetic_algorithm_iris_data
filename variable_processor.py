from function_generator import FunctionGenerator
from random import randint


class VariableProcessor:
	def getFunctions(self, num_func):
		generator = FunctionGenerator()
		func_list = []
		for _ in range(num_func):
			func_list.append(generator.getFunction(1, randint(0, 20)))
		return func_list
