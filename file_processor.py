from re import match


class FileProcessor:
	def readFile(self, passed_file):
		data_list = []
		for i, l in enumerate(passed_file):
			data_list.append(l.strip().split(","))
		return data_list

	def retrieveData(self, data):
		num = "num"
		string = "string"
		data_dict = {
			num: [],
			string: []
		}
		for var in data[:-1]:
			if var.isdigit() or match("^\d+?\.\d+?$", var) is not None:
				data_dict[num].append(float(var))
			else:
				data_dict[string].append(var)
		return (data_dict, data[-1])
