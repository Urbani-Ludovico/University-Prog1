class NumeriPrimi(object):
    def __init__(self, length: int):
        self.length = length
        
    def __iter__(self):
        self.iter = 0
        self.current = 1
        return self
        
    def __next__(self):
        self.iter += 1
        if self.iter > self.length:
            raise StopIteration
        
        while True:
            self.current += 1
            is_prime = True
            for item in range(2, self.current):
                if self.current % item == 0:
                    is_prime = False
                    break
            
            if is_prime:
                break
        
        return self.current
    
cl = NumeriPrimi(10)
for item in cl:
    print(item)