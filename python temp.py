'''
Author:Laura Rose Rubin
Date:25-10-2024
Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c/5=f−32/9
'''
temp_1=int(input("enter the temperature"))
scale=input(" is this in (C)elsius or (f)ahrenheit?")
if scale=="C":
    print(temp_1,"celsius:",(9/5*temp_1)+32,"fahrenheit")
else:
    print(temp_1,"fahrenheit",5/9*(temp_1-32),"celsius")