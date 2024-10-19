'''
Author:Laura Rose Rubin
Date:19-10-2024
Description:Create, concatenate, and print a string and access a sub-string from a given string
'''



first_name = input("enter your first name")
last_name = input("enter your last name")
full_name=first_name+" "+last_name
print(full_name)
first_name_length=len(first_name)
extracted_last_name=full_name[:first_name_length]
print(extracted_last_name)



