'''
Author:Laura Rose Rubin
Date:29-11-2024

'''
def right_triangle(side):
    side.sort()
    if side[2]**2==side[0]**2+side[1]**2:
        return True
    return False
side=[]
side.append(int(input(" Enter the length of side1:")))
side.append(int(input(" Enter the length of side2:")))
side.append(int(input(" Enter the length of side3:")))
if right_triangle(side):
    print("it is a right triangle")
else:
    print(" it is not a right triangle")


