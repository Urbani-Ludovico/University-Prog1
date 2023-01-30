
from math import e as e_const
from math import pi

class Funzione(object):
    def __init__(self, func = None):
        self.func = func
    
    def eval(self, x: int|float):
        if (self.func != None):
            return self.func(x)
        
        raise NotImplementedError()
    
    def calcola_integrale(self, a: int|float, b: int|float, M: int|float):
        if M == 0:
            return M
        
        h = (b - a) / M
        Sm = 0
        for i in range(M):
            Sm += self.eval(a + i * h)
        
        
        return Sm * h
    

for n, item in enumerate([
    ((lambda x: x**2 - 2 * x), 1, 0),
    ((lambda x: e_const**(2*x)), pi, -pi/2),
    ((lambda x: x/(1+x**2)), 2, -2),
]):
    print("\n\nFUNZIONE %i" % (n+1))
    f = Funzione(item[0])
    for M in range(0, 1000001, 10000):
        print("M = %i :  %.10f" % (M, f.calcola_integrale(item[1], item[2], M)))