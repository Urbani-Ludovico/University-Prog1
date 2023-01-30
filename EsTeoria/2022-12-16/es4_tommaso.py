#iteratore che stampa i primi n numeri primi

def isprime(n):
    flag = True
    if n==1:
        return False
    for i in range (2,n):
        if n%i == 0:
            flag = False
    return flag

class NumPrimi():
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.numero_primi = 0
        self.contatore = 1
        return self

    def __next__(self):
        if self.numero_primi <= self.max:
            if isprime(self.contatore):
                self.numero_primi += 1
                da_rit = self.contatore
                self.contatore += 1
                return da_rit
            else:
                self.contatore += 1
        else:
            raise StopIteration

obj = NumPrimi(20)
[print(i) for i in obj]