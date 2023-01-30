
class ExamException(Exception):
    pass

class CSVFile(object):
    def __init__(self, path = None):
        self.path = path
        
    def get_data(self):
        file = self.open()
        data = [item.split(",") for item in file.read().split("\n")]
        file.close()
        
        return data
    
    def open(self):
        try:
            return open(self.path, "r")
        
        except FileNotFoundError as e:
            raise ExamException(str(e))
        
        except TypeError as e:
            # When open receive data different from string
            raise ExamException(str(e))
    
    
class CSVTimeSeriesFile(CSVFile):
    def __init__(self, name = None):
        super().__init__(path = name)
        
    def get_data(self):
        data = super().get_data()
        purified_data = []
        
        for item in data:
            new_row = []
            to_add = True
            try:
                date = item[0]
                try:
                    date = int(date)
                except ValueError as e:
                    # For dates in format float
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
        
        return purified_data

class Epoch(object):
    def __init__(self, epoch = None):
        self.epoch = epoch
        self.day = self.date_get_day(self.epoch)
        
    def date_get_day(self, date):
        return date - (date % 86400)
    
    def __lt__(self, other): # less than in epoch comparison
        if isinstance(other, Epoch):
            return self.epoch < other.epoch
        return False
    
    def __gt__(self, other): # greater than in epoch comparison
        if isinstance(other, Epoch):
            return self.epoch > other.epoch
        return True
        

class DayTemps(object):
    def __init__(self):
        self.data = {}
        self.days = []
        
    def add(self, day, temp):
        if not day in self.days:
            self.days.append(day)
            self.data[day] = []
        self.data[day].append(temp)
        

def compute_daily_max_difference(data):
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


# x = CSVTimeSeriesFile("data.csv")
# print(x.get_data())
# d = compute_daily_max_difference(x.get_data())
# for item in d:
#     print(item)