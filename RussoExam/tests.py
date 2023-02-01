
import unittest

from esame import ExamException, CSVFile, CSVTimeSeriesFile, Epoch, DayTemps, compute_daily_max_difference


# @unittest.skip
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


# @unittest.skip
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
       
    def test_temps_not_ordered(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile8.csv")
        self.assertRaises(ExamException, c.get_data)
       
    def test_temps_duplicate(self):
        c = CSVTimeSeriesFile("data_test_CSVTimeSeriesFile9.csv")
        self.assertRaises(ExamException, c.get_data)
       
        
# @unittest.skip
class TestEpoch(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(Epoch(86410).day, 86400)
        
    def test_correct2(self):
        self.assertEqual(Epoch(172800).day, 172800)
        
    def test_correct3(self):
        self.assertEqual(Epoch(-100).day, 0)
        
    def test_correct4(self):
        self.assertEqual(Epoch(-86410).day, -86400)
        
    def test_lt_(self):
        self.assertTrue(Epoch(10) < Epoch(86410))
        
    def test_lt_2(self):
        self.assertTrue(Epoch(-100) < Epoch(100))
        
    def test_lt_3(self):
        self.assertFalse(Epoch(86410) < Epoch(10))
    
    def test_lt_4(self):
        self.assertFalse(Epoch(100) < Epoch(100))
        
    def test_gt_(self):
        self.assertTrue(Epoch(86410) > Epoch(10))
        
    def test_gt_2(self):
        self.assertTrue(Epoch(100) > Epoch(-100))
        
    def test_gt_3(self):
        self.assertFalse(Epoch(10) > Epoch(86410))
        
    def test_gt_4(self):
        self.assertFalse(Epoch(100) > Epoch(100))
        
        
# @unittest.skip
class TestDayTemps(unittest.TestCase):
    def test_correct(self):
        dt = DayTemps()
        dt.add(86400, 35.0)
        self.assertEqual(dt.data, {86400: [35.0]})
        self.assertEqual(dt.days, [86400])
        
    def test_correct(self):
        dt = DayTemps()
        dt.add(86400, 35.0)
        dt.add(172800, 25.0)
        dt.add(86400, 20.0)
        self.assertEqual(dt.data, {86400: [35.0, 20], 172800: [25.0]})
        self.assertEqual(dt.days, [86400, 172800])
        

# @unittest.skip
class TestCompute(unittest.TestCase):
    def test_purify(self):
        self.assertEqual(compute_daily_max_difference([["3545",3], [3546.5, 5.0]]), [2.0])
        
    def test_purify_none(self):
        self.assertEqual(compute_daily_max_difference([["3545",3]]), [None])
        
    def test_purify_empty(self):
        self.assertEqual(compute_daily_max_difference([]), [])
        
    def test_purify_empty2(self):
        self.assertEqual(compute_daily_max_difference([["ciao",3]]), [])
        
    def test_correct(self):
        self.assertEqual(compute_daily_max_difference([[1675077364, 25.30], [1675077387, 27.24]]), [27.24-25.30])
       
    def test_correct2(self):
        self.assertEqual(compute_daily_max_difference([[100, -4.35], [1675077364, 25.30], [1675077387, 27.24]]), [None, 27.24-25.30])
        
    def test_correct_negative(self):
        self.assertEqual(compute_daily_max_difference([[1675077364, -4.13], [1675077387, 27.24]]), [27.24-(-4.13)])
       
        
if __name__ == '__main__':
    unittest.main()