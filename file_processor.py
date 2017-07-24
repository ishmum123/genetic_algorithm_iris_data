class FileProcessor:
	def readFile(self, passed_file):
		data_list = []
		for i, l in enumerate(passed_file):
			data_list.append(l.strip().split(","))
		return data_list

	def retrieveData(self, data):
		string_data = []
		num_data = []
		for var in data[:-1]:
			if isinstance(var, int):
				num_data.append(var)
			else:
				string_data.append(var)
		return ((string_data, num_data), data[-1])
