# del key in oops
class student:
    def __init__(self, name):
        self.name=name

s1 = student("swarup")

print(s1.name)
del s1.name
print(s1.name)

#privat and public 

class creat:
    def __init__(self,acc_name,acc_password):
        self.acc_name=acc_name
        self.__acc_password= acc_password

        def resetacc(self):
            print(self.__acc_password)
            

user=creat("swarup",123456)
print(user.acc_name)  
print(user.resetacc())    



# inheritance using constructer 
class car:
    def __init__(self, window, door, engin):
        self.window=window
        self.door=door
        self.engin=engin
    
    def driving(self):
        print(" i am driving bmw")

# here bmw is inheriting  from car 
class bmw(car):
    def __init__(self, window, door, engin,speed):
        super().__init__(window, door, engin)
        self.speed=speed

    def self_driving(self):
        print(" it is self driving car")


new_model=bmw(4,6,'v8',400)
print(new_model.door, new_model.window)
new_model.driving()
new_model.self_driving()


#  multiple inheritance 
class a:
    vara="here is vlaue of A"

class b:
    varb="here is value of b"


class c(a ,b ):
    varc="here is valuse of c"

c1= c()
print(c1.vara)
print(c1.varc)


#multilevel inheritance 
class multi:
    @staticmethod
    def first():
        print("here is first")

    @staticmethod
    def sec():
        print("here is second") 

class new (multi):
    def __init__(self ,name ):
        self.name =name 


sname= new("swarup")  
print (sname.name)
print(sname.sec())   

class again (new):
    def __init__(self, ssname):
        self.ssname=ssname

newname= again("hari")    
print(newname.first())  



# inheritance in dataclass 
from dataclasses import dataclass
@dataclass

class person :
    name:str
    age:int

@dataclass
class employe(person):
    emp_id:int
    emp_dprt: str

emp1=employe('swarup', 22, 123, 'compueter science')
print(emp1.name, emp1.age, emp1.emp_dprt)



