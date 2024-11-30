'''
Author:Laura Rose Rubin
Date:30-11-2024
'''


num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))

def max_number(num1, num2, num3):
    if(num1>num2) and (num1>num3):
        return num1
    elif(num2>num3):
        return num2
    else:
        return num3
print("max_number=",max_number(num1,num2,num3))