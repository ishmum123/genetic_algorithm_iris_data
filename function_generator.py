from math import exp, log, log10, log1p, sqrt, sin, cos, pow, fmod


class FunctionGenerator:
	def getFunction(self, num_arg, func_num):
		func = None
		def m_rnd(x):
			return round(x, 2)
		if num_arg == 1: 
			if func_num == 0:
				func = lambda x: x + 1
			elif func_num == 1:
				func = lambda x: m_rnd(sqrt(x))
			elif func_num == 2:
				func = lambda x: m_rnd(exp(x))
			elif func_num == 3:
				func = lambda x: m_rnd(exp(-x))
			elif func_num == 4:
				func = lambda x: m_rnd(log10(x))
			elif func_num == 5:
				func = lambda x: m_rnd(log1p(x))
			elif func_num == 6:
				func = lambda x: m_rnd(cos(x))
			elif func_num == 7:
				func = lambda x: m_rnd(sin(x))
			elif func_num == 8:
				func = lambda x: m_rnd(pow(x, 2))
			else:
				func = lambda x: x
		elif num_arg == 2:
			if func_num == 0:
				func = lambda x, y: x + y
			elif func_num == 1:
				func = lambda x, y: x - y
			elif func_num == 2:
				func = lambda x, y: m_rnd(x * y)
			elif func_num == 3:
				func = lambda x, y: m_rnd(x / y)
			elif func_num == 4:
				func = lambda x, y: m_rnd(pow(x, y))
			elif func_num == 5:
				func = lambda x, y: m_rnd(pow(y, x))
			elif func_num == 6:
				func = lambda x, y: m_rnd(log(y, x))
			elif func_num == 7:
				func = lambda x, y: m_rnd(log(x, y))
			elif func_num == 8:
				func = lambda x, y: m_rnd(fmod(y, x))
			elif func_num == 9:
				func = lambda x, y: m_rnd(fmod(x, y))
			elif func_num == 10:
				func = lambda x, y: y
			else:
				func = lambda x, y: x
		else:
			raise ValueError
		return func
