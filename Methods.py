# Methods
# Example 
class Square():
    edge = 4
    pass
    def area_calculated(self):
        self.area = self.edge * self.edge 
        print("Area",self.area)
s1 = Square()
print(s1.area_calculated())
s1.edge = 7
print(s1.area_calculated())

""" Methods vs Funtion"""
#Example
class employee(object):
    age = 30
    salary = 10000
    def salary_age_ratio_calculater(self):
        self.sarc = float(self.age/self.salary)
        print("Salary Age Ratio Calculated Value: ",self.sarc)
A = employee()
A.salary_age_ratio_calculater()
#Function
def salar_age_calculater(salary,age):
    result = float(age / salary)
    print(result)
salar_age_calculater(3000,30)
# Functions look like more effective but not like that. u will see after topics.