#make a class to calculate slope/distance of a line.
class SlopeDistance():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((y2 - y1) / (x2 - x1))
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)**2)**.5

coord1 = (5,6)
coord2 = (3,100)
slopeDist = SlopeDistance(coord1,coord2)
print(slopeDist.distance())
print(slopeDist.slope())
    
#make a class that calculates the surface area and volume of a cynlinder
class Cylinder:
    def __init__(self,height,radius):
        self.height = height
        self.radius = radius
    def surfaceArea(self):
        pi = 3.1415
        h = self.height
        r = self.radius
        return 2*pi*r*h + 2*pi*r**2
    def volume(self):
        pi = 3.1415
        h = self.height
        r = self.radius
        return pi*r**2*h
cylinder = Cylinder(5,6)
print(cylinder.volume())
print(cylinder.surfaceArea())

#create a bank account class with owner/balance and methods deposit/withdraw
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,addmoney):
        self.balance += addmoney
        print(f'Your balance is now: {self.balance}')
    def withdraw(self,takemoney):
        if self.balance < takemoney:
            print(f'You dont have enough money {self.owner}')
        else:
            self.balance -= takemoney
            print(f'Your balance is now: {self.balance}')
accountowner = BankAccount('Tim',700)
accountowner.deposit(100)
accountowner.withdraw(30)
print(accountowner.balance)
