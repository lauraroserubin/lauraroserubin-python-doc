'''
Author:Laura Rose Rubin
Date:29-11-2024
Description:Program to check whether the given number is a valid mobile number or not using functions


'''
def mobile_num(number):
    if len(number)==10 and number[0] in ["9", "8", "7"]:
        return True
    return False
number=input("enter the number")
if mobile_num(number):
    print("it is valid mobile number")
else:
    print("it is an invalid mobile number")