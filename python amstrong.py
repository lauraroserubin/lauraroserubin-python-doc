'''
Author:Laura Rose Rubin
Date:25-10-2024
Description:python program to find whether a number is armstrong or not
'''



num=int(input("enter a number"))

sum=0
while(num>0):
    r=sum%10
    sum = sum+r**3
    num=num//10
if(sum==num):
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
