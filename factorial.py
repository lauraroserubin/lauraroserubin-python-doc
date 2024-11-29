'''
Author:Laura Rose Rubin
Date:29-11-2024
Description:Program to find the factorial of a number using Recursion.

'''
num=int(input("Enter a number"))
def recursive_factorial(num):
        if num==1:
            return 1
        else:
            return num*recursive_factorial(num-1)
print(recursive_factorial(num))

