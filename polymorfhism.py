# Polymorfhism 
# Same deffinition - but different usage
# Exapmle

class Employee:
    def raise_function(self):
    
        raise_rate = 0.1
        result = 100+100*raise_rate
        print("Salary" ,result)
class CompEng:
    def raise_funtion(self):
        raise_rate = 0.2
        result = 100+100*raise_rate
        print("CompEng: " , result)
class MechatronicsE:
    def raise_funtion(self):
        raise_rate = 0.5
        result = 100 + 100*raise_rate
        print("MechatronicE: ",result)

a = Employee()
a.raise_function()
b = CompEng()
b.raise_funtion()
c = MechatronicsE()
c.raise_funtion()