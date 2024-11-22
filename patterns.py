'''
Author:Laura Rose Rubin
Date:22-11-2024
'''


n=int(input("enter number of rows"))
for i in range (n):
    for j in range(i+1):
        print("*",end="")
    print("")

n=int(input("enter number of rows"))
for i in range (n):
    for j in range(n-i):
        print("*",end="")
    print("")

n=int(input("enter number of rows"))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
n=int(input("enter number of rows"))
for i in range(n, 0,-1):
    for j in range(n - i):
        print(" ",end="")
    for k in range (i*2-1):
        print("*",end="")
    print()
