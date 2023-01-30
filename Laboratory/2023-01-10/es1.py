

class CSVFile(object):
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        l = []
        file = open(self.name, "r").read().split("\n")
        if file[0][:4] == "Date":
            file.pop(0)
        for item in file:
            items = item.split(",")
            if len(items) > 1:
                l.append(items)
        return l
            
class NumericalCSVFile(CSVFile):
    def get_data(self):
        data = super().get_data()
        dataNum = []
        for item in data:
            try:
                dataNum.append(float(item[1]))
            except ValueError:
                print(item)
                print("Errore")
        return dataNum
    
class Model(object):
    def __init__(self, period = 3, window = 2/3):
        self.period = period
        self.window = window
        
    def evaluate(self, data):
        raise NotImplementedError("Not implemented")
    
    def fit(self, data):
        raise NotImplementedError("Not implemented")
    
    def predict(self, data):
        raise NotImplementedError("Not implemented")
    
    
class IncrementModel(Model):
    
    def evaluate_predict_func(self, datafit, datatest):
        return self.predict(datatest, period = self.period)
    
    def evaluate(self, data):
        separator = round(len(data) * self.window)
        datafit = data[:separator]
        datatest = data[separator:]
        #print(datafit, len(datafit))
        #print(datatest, len(datatest))
        
        abs_error = 0
        abs_error_count = 0
        for item in range(0, len(datatest) - self.period-1):
            p = self.evaluate_predict_func(datafit, datatest[item:item+self.period])
            abs_error += abs(p - datatest[item+self.period+1])
            abs_error_count += 1
            
        if abs_error_count == 0:
            return 0
        return abs_error / abs_error_count
    
    def prediction_checkData(self, data):
        if not isinstance(data, list):
            self.prediction_typeError()
            
        if len(data) < 2:
            self.prediction_typeError()
        
        return True
    
    def prediction_typeError(self):
        raise TypeError("Prediction: input data in wrong format")
        
    def predict(self, data, period=3):
        if self.prediction_checkData(data):
            sum_dev = 0
            
            dt = data[-period:]
            for n, item in enumerate(dt):
                if n != period-1:
                    sum_dev += dt[n+1] - item
            
            prediction = sum_dev / (period-1)
            
            return data[-1] + prediction
        

class FitIncrementModel(IncrementModel):
    
    def evaluate_predict_func(self, datafit, datatest):
        return self.fit(datafit, datatest, period = self.period)
    
    def fit(self, datafit, datatest, period = 3):
        cnt = 0
        diff = 0
        for item in range(0, len(datafit)-1):
            diff += datafit[item+1] - datafit[item]
            cnt += 1
            
        if cnt == 0:
            return 0
        return diff / cnt + self.predict(datatest, period = period)
        
        
    
# data = NumericalCSVFile("shampoo_sales.csv").get_data()

# inc_mod = IncrementModel()
# print("Increment: ", inc_mod.evaluate(data))

# fit_mod = FitIncrementModel()
# print("Fit: ", fit_mod.evaluate(data))