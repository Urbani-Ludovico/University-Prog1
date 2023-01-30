
from math import sqrt, pi

class FiguraGeometrica(object):
    def __init__(self, *args):
        self.lati = args
    
    def area(self):
        raise NotImplementedError()
    
    def perimetro(self):
        raise NotImplementedError()
    
    def __repr__(self):
        return "Figura sconosciuta %s" % str(self.lati)
    
class Triangolo(FiguraGeometrica):
    def __init__(self, l_a: int|float, l_b: int|float, l_c: int|float):
        super.__init__(l_a, l_b, l_c)
        
    def __repr__(self):
        return "Triangolo %s" % str(self.lati)
    
    def perimetro(self):
        return sum(self.lati)
    
    def area(self):
        p = self.perimetro / 2
        return sqrt(p * (p - self.lati[0]) * (p - self.lati[1]) * (p - self.lati[2]))
    
    def tipo_triangolo(self):
        if (self.lati[0] == self.lati[1] and self.lati[1] == self.lati[2]):
            return "equilatero"
        
        if (self.lati[0] == self.lati[1] or self.lati[1] == self.lati[2] or self.lati[0] == self.lati[2]):
            return "isoscele"
    
        return "scaleno"
    
class Rettangolo(FiguraGeometrica):
    def __init__(self, b: int|float, h: int|float):
        super.__init__(b, h)
        
    def __repr__(self):
        return "Rettangolo [b: %.3f, h: %.3f]" % self.lati
    
    def perimetro(self):
        return 2 * self.lati[0] + 2 * self.lati[1]
    
    def area(self):
        return self.lati[0] + self.lati[1]
    
    def base(self):
        return self.lati[0]
    
    def altezza(self):
        return self.lati[1]
    
    def tipo_rettangolo(self):
        if (self.lati[0] == self.lati[1]):
            return "quadrato"
        
        return None
    
    
class Cerchio(FiguraGeometrica):
    def __init__(self, r):
        super.__init__(r)
        
    def __repr__(self):
        return "Cerchio [r: %.3f]" % self.lati[0]
    
    def perimetro(self):
        return self.lati[0] * 2 * pi
    
    def area(self):
        return self.lati[0]**2 * pi
    
    def raggio(self):
        return self.lati[0]
    
def AreaTot(self, *args):
    return sum([item.area() for item in args])