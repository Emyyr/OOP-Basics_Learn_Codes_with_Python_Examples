# İnitliazer and Constracter. 
class Animal(object):
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.species = c
    def get_information(self):
        print(f"Information :{self.name} , {self.age} , {self.species}")

a1 = Animal("Cat","7","Homodens")
a1.get_information()

#Now we can add new objects and we can create new function with new veriables
Trex = Animal("Bird" , "10000" , "Old")
Trex.get_information()

"""----------------------------------------------------------------------------------------------------------"""

# Example for described so far
# Calculator 
class Calculator():
    def __init__(self,value_1,value_2):
        self.value1 = value_1 
        self.value2 = value_2
    def additional(self):
        return float(self.value1 + self.value2)
    def subtraction(self):
        return float(self.value1 - self.value2)
    def multiplaction(self):
        return float(self.value1*self.value2)
    def divide(self):
        return float(self.value1 / self.value2)
    def force(self):
        return float(self.value1**self.value2)
number_1 = 0
number_2 = 0
print("Lütfen işlem yapamk istediğiniz değerleri giriniz:")
number_1=int(input(f"Input first number:".format(number_1)))
number_2=int(input(f"Input second number:".format(number_2)))
result = Calculator(number_1,number_2)

print("----------Hesaplanıyor-----------")
workspace = input("Hangi işlemi yapmak isterseniz karşılığında bulunan sayıyı girininiz\n: Toplama-1 \n Cıkartma-2 \n Carpma-3\n Bölme-4 \n Üs işlemi- 5".format(workspace))
if workspace == "1":
    print(result.additional())
elif workspace=="2":
    print(result.subtraction())
elif workspace=="3":
    print(result.multiplaction())
elif workspace=="4":
    print(result.divide())
elif workspace=="5":
    print(result.force())
else: 
    print("Lütfen geçerlli bir eğer giriniz!")
    