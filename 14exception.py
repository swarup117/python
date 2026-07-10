#exception handling
#Exception hadle alltypes of exception 
#1
try:
    a=b
except Exception as ex:
    print(ex)
#name 'b' is not defined

#2
try:
    a=1
    b="s"
    c=a+b
except Exception as ex:
    print(ex)
#unsupported operand type(s) for +: 'int' and 'str'

#try --->  else -->  finally
try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number")) 
    c=a/b
except Exception as ex:
    print(ex)
else:
    print(c)
# else will only executed when  there is no exception 
finally:
    print("this will execte anyway")   
#finally will always executed     