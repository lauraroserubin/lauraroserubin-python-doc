'''
Author:Laura Rose Rubin
Date:25-10-2024
Description:to find sum of digits of a number
'''



number=int(input("enter a number"))
sum_of_digits=0
while number>0:
    remainder = number%10
    sum_of_digits = sum_of_digits+remainder
    number = number//10
print("sum of digits of the given number:",sum_of_digits)