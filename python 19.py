'''
Author:Laura Rose Rubin
Date:19-10-2024
Description:Simple desktop calculator using Python. Only the five basic arithmetic operators
'''



num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
num_add=num1+num2
print("the sum of num1 and num2 is:",num_add)
num_sub=num2-num1
print("the difference when num2 is subtracted from num1 is:",num_sub)
num_mul=num1*num2
print("the product of num1 and num2 is:",num_mul)
num_div=num1/num2
print("the quotient when num1 is divided by num2 is:",num_div)
num_rem=num1%num2
print("the remainder when num1 is divided by num2 is:",num_rem)
num_com=(num1+num2)*num3/2
print("the result of (num1+num2)*num3/2 is:",num_com)