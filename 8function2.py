# #Lambda (when function is small and recursice is not needed , 
# # lambda it self return value)

# square= lambda x :x*x
# print(square(2))

# square= lambda x :x**3
# print(square(2))

# add= lambda x,y :x+y
# print(add(2,3))


# # high order function 
# # function using function

# def sq(x):
#     return x*x

# def cal(func, number):
#     return func(number)
# print (cal(sq,5))

# using in pandas
import pandas as pd

df = pd.DataFrame({
    "Salary": [30000, 45000, 50000]
})

df["Bonus"] = df["Salary"].apply(lambda x: x * 1.10)
print(df)
