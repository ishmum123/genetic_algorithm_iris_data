class FunctionGenerator:
	def getFunction(self, num_arg):
		func = None
		if num_arg == 1: 
			func = lambda x: x + 1
		elif num_arg == 2:
			func = lambda x, y: x + y
		else:
			raise ValueError
		return func
