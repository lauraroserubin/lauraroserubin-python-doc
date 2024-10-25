'''
Author:Laura Rose Rubin
Date:25-10-2024
Description:Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
'''
num_1=int(input("enter first number:"))
num_2=int(input("enter second number:"))
num_3=int(input("enter third number:"))
if num_1>num_2 and num_1>num_3:
    print(num_1," is greater than the other two")
elif num_2>num_3:
    print(num_2," is greater than the other two")
else:
    print(num_3," is greater than the other two")

