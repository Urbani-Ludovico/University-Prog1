class MyPower(object):
    def __init__(self, a):
        self.a = a
    
    def __iter__(self):
        self.it = 0
        return self
    
    def __next__(self):
        if self.it > self.a:
            raise StopIteration
        
        if (self.it == 0):
            v = "+inf"
        else:
            v = 3**(self.it + 1) / self.it
        self.it += 1
        return v
    
    def mean_pow_a(self):
        s = 0
        c = 0
        for item in self:
            s += item
            c += 1
        if c == 0:
            raise Exception
        return s/c
    
c = MyPower(4)

for item in c:
    print(item)
    
print(c.mean_pow_a())
    
        