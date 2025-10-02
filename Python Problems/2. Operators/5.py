# 5.Take three numbers and find the largest using comparison operators.

num1=input("enter the first number- ")
num2=input("enter the second number- ")
num3=input("enter the third number- ")


num1=int(num1)
num2=int(num2)
num3=int(num3)

if(num1 >= num2 and num1 >= num3):
    print(num1, "is largest")
elif(num2 >= num1 and num2 >= num3):
    print(num2, "is largest")
else:
    print(num3, "is largest")


