
class Model(object):
    def fit(self, data):
        raise NotImplementedError("Not implemented")
    
    def predict(self, data):
        raise NotImplementedError("Not implemented")
    
    
class IncrementModel(Model):
    
    def prediction_checkData(self, data):
        if not isinstance(data, list):
            self.prediction_typeError()
            
        if len(data) < 2:
            self.prediction_typeError()
        
        return True
    
    def prediction_typeError(self):
        raise TypeError("Prediction: input data in wrong format")
        
    def predict(self, data, periods=3):
        if self.prediction_checkData(data):
            sum_dev = 0
            
            dt = data[-periods:]
            for n, item in enumerate(dt):
                if n != periods-1:
                    sum_dev += dt[n+1] - item
            
            
            prediction = sum_dev / (periods-1)
            
            return data[-1] + prediction
        
# cl = IncrementModel()
# print(cl.predict([50, 52, 60]))