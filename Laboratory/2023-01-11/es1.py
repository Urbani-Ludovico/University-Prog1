
class ExamException(Exception):
    pass
0
class MovingAverage(object):
    def __init__(self, window):
        if not isinstance(window, int) or window < 1:
            raise ExamException("window wrong")
        self.window = window
        
    def compute(self, data):
        self.check_data(data)
        
        avereges = []
        for item in range(0, len(data) - self.window + 1):
            s = None
            try:
                s = self.list_average(data[item:item + self.window])
            except TypeError as e:
                raise ExamException(str(e))
            if s != None:
                avereges.append(s)
        return avereges
            
    def list_average(self, data):
        return sum(data) / len(data)
        
    def check_data(self, data):
        if not isinstance(data, list):
            raise ExamException("dataset must be of type list")
        
        if len(data) == 0:
            raise ExamException("no data submitted")
        
        if len(data) < self.window:
            raise ExamException("too few data submitted")
        
moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result)