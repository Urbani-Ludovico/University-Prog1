
import unittest

from esame import ExamException, CSVFile, CSVTimeSeriesFile

class TestCSVFile(unittest.TestCase):
    
    def test_open_type(self):
        c = CSVFile()
        self.assertRaises(ExamException, c.open)
        
    def test_open_type2(self):
        c = CSVFile(ExamException)
        self.assertRaises(ExamException, c.open)
        
    def test_open_not_found(self):
        c = CSVFile("data_not_exists.csv")
        self.assertRaises(ExamException, c.open)
        
    def test_get_data_empty(self):
        c = CSVFile("data_test_CSVFile.csv")
        self.assertEqual(c.get_data(), [[""]])
        
    def test_get_data_empty2(self):
        c = CSVFile("data_test_CSVFile2.csv")
        self.assertEqual(c.get_data(), [[""], [""]])
        
    def test_get_data_twolines(self):
        c = CSVFile("data_test_CSVFile3.csv")
        self.assertEqual(c.get_data(), [["3"], ["5", "b"]])


class TestCSVTimeSeriesFile(unittest.TestCase):
    def test_correct(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile.csv")
        self.assertEqual(c.get_data(), [[1551398400, 21.5], [1551402000, 21.4], [1551405600, 21.3]])
        
    def test_less_one_temp(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile2.csv")
        self.assertEqual(c.get_data(), [[1551398400, 21.5], [1551405600, 21.3]])
        
    def test_one_temp_null(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile3.csv")
        self.assertEqual(c.get_data(), [[1551398400, 21.5], [1551405600, 21.3]])
    
    def test_one_temp_string(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile4.csv")
        self.assertEqual(c.get_data(), [[1551398400, 21.5], [1551405600, 21.3]])

    def test_one_date_string(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile5.csv")
        self.assertEqual(c.get_data(), [[1551398400, 21.5], [1551402000, 21.4]])
        
    def test_dates_float(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile6.csv")
        self.assertEqual(c.get_data(), [[1551398400, 21.5], [1551402000, 21.4], [1551405600, 21.3]])
        
    def test_temps_int(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile7.csv")
        self.assertEqual(c.get_data(), [[1551398400, 21], [1551402000, 22], [1551405600, 23]])
        
        
if __name__ == '__main__':
    unittest.main()