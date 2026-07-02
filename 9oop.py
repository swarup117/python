#oop concept in python 

class student:

    collage_name="utech"
    #constructer
    def __init__(self,name,mark):# here  name and mark are the  feature
        self.name=name
        self.mark=mark
        print("adding new student")

s1= student("swarup",98)
print(s1.name ,s1.mark) 

s2= student("raja",95)
print(s2.name ,s2.mark, s2.collage_name) 


# best way to do object oriented programmin in python
#using dataclass so that code we neednot need to make constructer
# no need of __init__
from dataclasses import dataclass

@dataclass
class person:
    Name:str
    Age:int
    Profession:str

person1=person('swarup',22,'data scientist')
print(person1.Name, person1.Age, person1.Profession)

#properties 
# datacalss (frozon=true) then its valuse wont change

@dataclass (frozen=True)
class point:
    x:int
    y:int

p1=point(3,4) 
print(p1.x,p1.y)   


 # class varibel and instance variable 
class Student:
    def __init__(self, name, age):
        self.name = name # instance variable 
        self.age = age  # instance variable 

s1 = Student("Swarup", 22)
s2 = Student("Ram", 20)    

#class variable with instance variable
class Student:

    college = "U-Tech"        # Class Variable

    def __init__(self, name, age):
        self.name = name      # Instance Variable
        self.age = age        # Instance Variable


s1 = Student("Swarup",22)
s2 = Student("Ram",20)

print(s1.name)
print(s1.age)
print(s1.college)

print()

print(s2.name)
print(s2.age)
print(s2.college)

# example take mark of student and print avg amrk

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        avg = sum(self.marks) / len(self.marks)
        print(f"Hi {self.name}, your average score is {avg}")


s1 = Student("Swarup", [78, 98, 93])
s1.get_average()