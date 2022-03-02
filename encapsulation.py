# Encapsulation - Encapsulation Direct External Access Restriction
class Bank_Accound():
    def __init__(self,name,money,adress):
        self.name = name
        self.money = money
        self.adress = adress 
m1 = Bank_Accound("Messi",1500,"Barcelona")
m2 = Bank_Accound("Neymar",3000,"Paris")

m2.money = m1.money + m2.money
m1.money = 0
m2.money , m1.money
# Example explain the result. We can not change some veriables. At least us. Coder must change this veriables. Or Banker :)
# We can add " __ " this trick what we External Access Restriction veriable.
class Bank_Accound():
    def __init__(self,name,money,adress):
        self.name = name
        self.__money = money
        self.adress = adress 
m1 = Bank_Accound("Messi",1500,"Barcelona")
m2 = Bank_Accound("Neymar",3000,"Paris")

m1.__money
# This code gives you Attribute Error!
# AttributeError: 'Bank_Accound' object has no attribute '__money'
# Money did private... We can not acces the money by any method.
# Everything o'right. But How can I change this private veriable? 
# You think like this "I have to change money. What can I do?"
#get and set mothods
class Bank_Accound():
    def __init__(self,name,money,adress):
        self.name = name
        self.__money = money
        self.adress = adress
    def getMoney(self):
        return self.__money
        pass
    def setMoney(self,amount):
        self.__money = amount
    def __increase(self): # Methots can be private veriable like this. We just can use this funciton in its class. 
        self.__money = self.__money + 500 
m1 = Bank_Accound("Messi",1500,"Barcelona")
m2 = Bank_Accound("Neymar",3000,"Paris")

m1.getMoney() , m1.setMoney(5000) , m1.getMoney()