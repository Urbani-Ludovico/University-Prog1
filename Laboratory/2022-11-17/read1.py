
def sum_csv(filename):
    file = open(filename, "r").read().split("\n")
    
    s = 0
    for item in file:
        item = item.split(",")
        try:
            s += float(item[1])
        except:
            pass
        
    if s != 0:
        return s
    return None

#print(sum_csv("shampoo_sales.csv"))