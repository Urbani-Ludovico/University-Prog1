
class CSVFile(object):
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        l = []
        file = open(self.name, "r").read().split("\n")
        for item in file:
            items = item.split(",")
            if items[0] != "Date" and len(items) == 2:
                l.append(items[:2])
        return l

# c = CSVFile("shampoo_sales.csv")
# print(c.get_data())