from unittest import TestCase
from file_processor import FileProcessor
from io import StringIO


class FakeFile(StringIO):
	pass

class TestFileProcessor(TestCase):
	def setUp(self):
		self.processor = FileProcessor()

	def getFakeFile(self, string):
		fake_file = FakeFile()
		fake_file.write(string)
		fake_file.seek(0)
		return fake_file

	def test_readFile_returns_list_of_words_from_file(self):
		test_str = "Test String"
		self.assertTrue(isinstance(self.processor.readFile(self.getFakeFile(test_str)), list))

	def test_readFile_returns_comma_separated_values_as_list(self):
		test_str = "test,str"
		self.assertEqual(self.processor.readFile(self.getFakeFile(test_str)), [["test", "str"]])

	def test_readFile_returns_each_line_as_new_list(self):
		test_str = "test,this\nline,str"
		self.assertEqual(self.processor.readFile(self.getFakeFile(test_str)), [["test", "this"], ["line", "str"]])

	def test_retrieveData_returns_dict_of_variables_and_last_element_as_desired_class(self):
		test_list = ["test_var1", "test_var2", "test_var3", "90", "test_class"]
		(data, des_class) = self.processor.retrieveData(test_list)
		self.assertTrue(isinstance(data, dict))
		self.assertEqual(des_class, "test_class")

	def test_retrieveData_returns_string_and_number_variables_in_separate_list(self):
		test_list = ["test_var1", "123.5samp", "sadkf123", "90", "test_var2", "3434.134", "test_class"]
		(data, des_class) = self.processor.retrieveData(test_list)
		self.assertEqual(data, {"string":["test_var1", "123.5samp", "sadkf123", "test_var2"],"num":[90, 3434.134]})
