# encapulation in oops
#  private protected and public


# it is private 
class creat:
    def __init__(self,acc_name,acc_password):
        self.acc_name=acc_name
        self.__acc_password=acc_password

    def show_detail(self):
        print(f"hi {self.acc_name},your password{self.__acc_password}")
            

user=creat("swarup",123456)
print(user.acc_name)  
print(user.show_detail()) # show detail is public with in class 
                          # we are able to display the private attributr 
print(user.__acc_password) # we cannot access the private attribute 
                            #outside the class


#protected  attribute should only use in derive calss(only1 _)

class creat1:
    def __init__(self,acc_name1,acc_password1):
        self.acc_name=acc_name1
        self._acc_password=acc_password1

class customer(creat1):
    def __init__(self, acc_name1, acc_password1):
        super().__init__(acc_name1, acc_password1)

    def show_detail(self):
        print(f"hi {self.acc_name},your password {self._acc_password}")    

cus1=customer('tharu', 117)
cus1.show_detail()
