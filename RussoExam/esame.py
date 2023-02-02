
from io import UnsupportedOperation

class ExamException(Exception):
    pass

class CSVFile(object):
    def __init__(self, path = None):
        """
            Args:
                str path = None: filename of dataset
        """
        self.path = path
        
    def get_data(self):
        """
            Open file and split data into rows and columns of strings

            Raises:
                ExamException

            Returns:
                list<list<str +>>
        """
        file = self.open()
        
        try:
            data = [item.split(",") for item in file.read().split("\n")]
            
        except TypeError as e:
            # File not readable
            raise ExamException(str(e))
        
        except UnsupportedOperation as e:
            # Data not iterable
            raise ExamException(str(e))
        
        except AttributeError as e:
            # Read data or item has not split attribute
            raise ExamException(str(e))
        
        file.close()
        
        return data
    
    def open(self):
        """
            Open and test file

            Raises:
                ExamException

            Returns:
                file stream
        """
        try:
            return open(self.path, "r")
        
        except FileNotFoundError as e:
            raise ExamException(str(e))
        
        except TypeError as e:
            # When open receive data different from string
            raise ExamException(str(e))
        
        except OSError as e:
            # Others os errors
            raise ExamException(str(e))
    
    
class CSVTimeSeriesFile(CSVFile):
    def __init__(self, name = None):
        """
            Args:
                str path = None: filename of dataset
        """
        super().__init__(path = name)
        
    def get_data(self):
        """
            Open and purify data

            Returns:
                list<list<int, float>>
        """
        data = super().get_data()
        return self.purify_data(data)
    
    def purify_data(self, data):
        """
            Purify data
            Keep only row that can be casted int [int, float], removing elements after index 1
            Function does not modify original data

            Args:
                list<list<str +>> data

            Raises:
                ExamException

            Returns:
                list<list<int, float>>
        """
        purified_data = []
        
        try:
            iter(data)
        except TypeError as e:
            raise ExamException(str(e))
        
        for item in data:
            new_row = []
            to_add = True
            try:
                date = item[0]
                try:
                    date = int(date)
                except ValueError as e:
                    # For dates in format float
                    # If neither this format match data, line will be removed in the expept of parent level
                    date = int(float(date))
                new_row.append(date)
                
                temperature = float(item[1])
                new_row.append(temperature)
                
            except IndexError as e:
                # Row has less than two elements
                to_add = False
                
            except ValueError as e:
                # Values are not in format [int, float]
                to_add = False
                
            if to_add:
                purified_data.append(new_row)
                
        self.check_order(purified_data)
        
        return purified_data
    
    def check_order(self, data, raise_exam = True):
        """
            Check if dataset is ordered and it does not have duplicate epoch
            
            Args:
                list<list<int, float>> data
                bool raise_exam: for disable raising

            Raises:
                ExamException

            Returns:
                bool
        """
        for n in range(1, len(data)):
            if not data[n-1] < data[n]:
                if raise_exam:
                    raise ExamException("File not ordered")
                return False
        return True
    
    def is_data_purified(self, data):
        """
            Check if data is purified:
                - list<list<int, float>>
                
            Args:
                list<list<any, any>> data

            Returns:
                bool
        """
        if not isinstance(data, (list, tuple)):
            return False
        
        for item in data:
            if not isinstance(item, (list, tuple)) or not isinstance(item[0], int) or not isinstance(item[1], float):
                return False
        
        return True

class Epoch(object):
    def __init__(self, epoch = None):
        """
            Args:
                int epoch
        """
        self.epoch = epoch
        self.day = self.date_get_day(self.epoch)
        
    def date_get_day(self, date):
        """
            Get epoch in time 00.00.00 of the same day

            Args:
                int date: epoch

            Returns:
                int
        """
        if date >= 0:
            return date - (date % 86400)
        return (abs(date) - (abs(date) % 86400) + 86400) * (-1)
    
    def __lt__(self, other):
        """
            self < other
            self less than other

            Args:
                Epoch other

            Returns:
                bool
        """
        if isinstance(other, Epoch):
            return self.epoch < other.epoch
        return False
    
    def __gt__(self, other):
        """
            self > other
            self greater than other

            Args:
                Epoch other

            Returns:
                bool
        """
        if isinstance(other, Epoch):
            return self.epoch > other.epoch
        return True
        

class DayTemps(object):
    def __init__(self):
        """
            Data collection
            Divide values in list of days and give a list of epochs of starting day
        """
        self.data = {}
        self.days = []
        
    def add(self, day, temp):
        """
            Add data to data collection

            Args:
                int day: epoch of day at time 00.00.00
                float temp
        """
        if not day in self.days:
            self.days.append(day)
            self.data[day] = []
        self.data[day].append(temp)
        

def compute_daily_max_difference(data):
    """
        Return a list of the temperature escursion list by day

        Args:
            list<list<any, any>> data: should be in format list<list<int, float>>

        Raises:
            ExamException

        Returns:
            list<float>
    """
    if not CSVTimeSeriesFile().is_data_purified(data):
        data = CSVTimeSeriesFile().purify_data(data)
    last_date = None
    day_data = DayTemps()
    
    for item in data:
        date = Epoch(item[0])
        
        if not date > last_date:
            raise ExamException("Incorect order or duplicate date")
        last_date = date

        day_data.add(date.day, item[1])
        
    output = []
    for day in day_data.days:
        if len(day_data.data[day]) < 2:
            output.append(None)
        else:
            # print(max(day_data.data[day]), min(day_data.data[day]))
            output.append(max(day_data.data[day]) - min(day_data.data[day]))
    
    return output