'''
Author:Laura Rose Rubin
Date:8\11\2024
Description:find the largest and smallest number from the list of numbers
'''



limit=int(input("enter the limit"))
number=int(input("enter a number"))
big=number
small=number
while limit>0:
    number=int(input("enter a number"))
    if number > big:
        big=number
    elif number < small:
        small=number
    limit = limit-1
    print(f"big={big}")
    print(f"small={small}")













