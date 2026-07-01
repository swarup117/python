# using function 
#description is important , sothat any can hover the function know about it

def welcome():
    """
    description : this function will show the welcome message 
    return : this function will return welcome meassage
    """
    return "good morning"

message= welcome()
print(message)
print(message +" hello every one")

#parameter  in function 
def even_odd_sum(lst):

    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return even_sum, odd_sum

sum1,sum2=even_odd_sum([1,3,2,4,5,6,45,6,7,98,84,34,2,5,77,98])
print(sum1,sum2)
        
# positional and keyword argumnt

def hello (name, age):
    print("hello"+ name + "you are" + str(age) + "years old")
    print(f"hello {name}, you are {age} year old")# here professional way
    # f says this strring contains variable in {} replace with arguments

hello("swarup",18)

#keyword argument 
def hello (name, age=22):
    
    print(f"hello {name}, you are {age} year old")# here professional way
    # f says this strring contains variable in {} replace with arguments

hello("swarup")

# better way to define positional and keyword argumnts
def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun("swarup", "tharu", age=22)