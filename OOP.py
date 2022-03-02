# Nesne Tabanlı Programlama
"""
Created by Emir Can
1.03.2022
This codes about OOP. 

"""
#CLASSES
"""
Sometimes we have to create any veraible for our purpose. However you can
created some classes. But sometimes we have to create what so many veriables to our project. 
Couse of that we use OOP. OOP facilitate like this problems.
Let's start.
"""
soccer_1_name = "Messi"
soccer_1_age = "35"
soccer_1_team = "Paris"

# if you save soccer player's informations like messi you don't have to write like this. 
# We use class

class Soccer(object): #or we can write class Soccer()
    #attribute = age,play team etc.
    #behevior  = forvet,goal etc.
    pass
# Attribute 
# Now try to add some attributes in our class

class Footboller():
    
    age=30
    team = "Galatasaray"
    pass
# add one veriable for footballer class
    
Ronaldo = Footboller()
print(Ronaldo.age)
print(Ronaldo.team),
# Try to change atrribute value 

Ronaldo.team = "Fenerbahce"
print(Ronaldo.team)
# We change a veriable but this is not propose.