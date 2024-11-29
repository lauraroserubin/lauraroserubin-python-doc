'''
Author:Laura Rose Rubin
Date:29-11-2024

'''

num1=int(input("enter the number"))
num2=int(input("enter the number"))
def recursive_mul(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+recursive_mul(num1,num2-1)
print(recursive_mul(num1,num2))
