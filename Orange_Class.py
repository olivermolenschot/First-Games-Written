
class Orange:
    def __init__(self,pickupDate,size,ripeness):
        self.date = pickupDate
        self.size = size
        self.ripeness = ripeness
    def printout(self):
        print(self.date,self.size,self.ripeness)

orange1 = Orange('27th','large','ready')
orange1.printout()

x = 10
y = x
x+=1

print(x is y)