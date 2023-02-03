
import unittest

from esame_sabatino import ExamException, CSVTimeSeriesFile, compute_daily_max_difference


class TestCSVTimeSeriesFile(unittest.TestCase):
    def test_open_type(self):
        c = CSVTimeSeriesFile()
        self.assertRaises(ExamException, c.get_data)
        
    def test_open_type2(self):
        c = CSVTimeSeriesFile(ExamException)
        self.assertRaises(ExamException, c.get_data)
        
    def test_open_not_found(self):
        c = CSVTimeSeriesFile("data_not_exists.csv")
        self.assertRaises(ExamException, c.get_data)

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
       
    def test_temps_not_ordered(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile8.csv")
        self.assertRaises(ExamException, c.get_data)
       
    def test_temps_duplicate(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile9.csv")
        self.assertRaises(ExamException, c.get_data)
        

class TestCompute(unittest.TestCase):
    def test_purify_empty(self):
        self.assertEqual(compute_daily_max_difference([]), [])
        
    def test_correct(self):
        self.assertEqual(compute_daily_max_difference([[1675077364, 25.30], [1675077387, 27.24]]), [27.24-25.30])
       
    def test_correct2(self):
        self.assertEqual(compute_daily_max_difference([[100, -4.35], [1675077364, 25.30], [1675077387, 27.24]]), [None, 27.24-25.30])
        
    def test_correct_negative(self):
        self.assertEqual(compute_daily_max_difference([[1675077364, -4.13], [1675077387, 27.24]]), [27.24-(-4.13)])
    
    def test_correct_tuple(self):
        self.assertEqual(compute_daily_max_difference(((1675077364, -4.13), (1675077387, 27.24))), [27.24-(-4.13)])
        
    def test_negative_epoch(self):
        self.assertEqual(compute_daily_max_difference([[-1000, 20], [-100, 25]]), [25-20])
        
    def test_negative_positive(self):
        self.assertEqual(compute_daily_max_difference([[-100, 10], [100, 10]]), [None, None])
        
        
        
if __name__ == '__main__':
    unittest.main()