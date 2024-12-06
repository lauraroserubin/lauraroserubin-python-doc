'''
Author:Laura Rose Rubin
Description:Recursive function to find the greatest common divisor of two positive numbers.
'''


def gcd(num1,num2):
    if num1%num2 == 0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1=int(input("enter a number"))
num2=int(input("enter a number"))
custom=gcd(num1,num2)
print(custom)