
class CSVFile(object):
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        l = []
        try:
            file = open(self.name, "r").read().split("\n")
            if file[0][:4] == "Date":
                file.pop(0)
            for item in file:
                items = item.split(",")
                if len(items) > 1:
                    l.append(items)
            return l
        except FileNotFoundError:
            print("Errore: file not found")
            
class NumericalCSVFile(CSVFile):
    def get_data(self):
        data = super().get_data()
        dataNum = []
        for item in data:
            try:
                dataNum.append([item[0]] + [float(item2) for item2 in item[1:]])
            except ValueError:
                print(item)
                print("Errore")
        return dataNum
        

# c = NumericalCSVFile("shampoo_sales2.csv")
# print(c.get_data())