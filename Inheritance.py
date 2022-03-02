# Miras/Inheritance 
# Code above subect of Inheritance
# We use super().__init__() 
# Making associations between classes
class Animal(object):
    def __init__(self):
        print("Animal is created")
    def toString(self):
        print("Animal")
    def walk(self):
        print("Animal walk!")
class Monkey(Animal):
    def __init__(self):
        super().__init__()
        print("Monket is created!")
    def climb(self):
        print("Monkey Climb")
class Bird(Animal):
    def __init__(self):
        super().__init__()
    def fly(self):
        print("Bird fly")


mon = Monkey()
mon.toString()
mon.walk()
mon.climb()

bird = Bird()
bird.toString()
bird.walk()
bird.fly()

"""----------------------------------------------------------------------------------------------------------"""
# Webside Example 
class Darkweb:
    def __init__(self,name,surname):
        self.name = name 
        self.surname = surname
    def loginfo(self):
        print(self.name + " " +self.surname)
    

class Web1(Darkweb):
    def __init__(self,name,surname,ids):
        Darkweb.__init__(self,name,surname)
        self.ids = ids 
    def login(self):
        print(self.name ," ", self.surname ," ",self.ids)


class Web2(Darkweb):
    def __init__(self,name,surname,e_mail):
        Darkweb.__init__(self,name,surname)
        self.e_mail = e_mail
    def login_2(self):
        print(self.name ," ", self.surname ," ",self.e_mail)

class web3(Darkweb):
    def __init__(self,name,surname,secure):
        Darkweb.__init__(self,name,surname)
        self.secure = secure
    def login_3(self):
        print(self.name +" "+ self.surname + " " + self.secure)


# it's like so simple and not neccesary but You can think general class will contain lots of veriable.
# So, it will be sensible.