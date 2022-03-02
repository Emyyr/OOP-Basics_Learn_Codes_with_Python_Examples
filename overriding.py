# Overriding
class Animal():
    def toString(self):
        print("Animal") 

class Donkey(Animal): 
    def toString(self):
        print("Donkey")

# 2 Class have same deffination(function). Which function  will be prefer ? 

a = Donkey()
a.toString() # Overriding function calls and Donkey use its funciton not Animal funciton.
    
ans_will_be  = "Donkey"