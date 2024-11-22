'''
Author:Laura Rose Rubin
Date:22-11-2024
'''
list_1=[1,2,3,4]
list_2=[5,6,7,8]
list_3=list_1+list_2
print(list_1)
print(list_2)
print(list_3)
even=[]
odd=[]
for numbers in list_3:
    if numbers%2==0:
     even.append(numbers)
     even.sort(reverse=True)
    else:
     odd.append(numbers)
     odd.sort(reverse=True)
print(even+odd)
