'''
Author:Laura Rose Rubin
Date:28-10-2024
Description:Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program
'''



while True:
      print(".\tcovert celsius to fahrenheit")
      print(".\tconvert fahrenheit to celsius")
      print(".\texit")
      choice=int(input("enter a choice:"))
      if choice ==1:
          temp_1=int(input("enter a temperature in celsius"))
          fah=(temp_1 * 9/5) + 32
          print(temp_1,"C in fahrenheit is",fah,"F")
      elif choice ==2:
          temp_2=int(input("enter a temperature in fahrenheit"))
          cel=(temp_2- 32) * 5/9
          print(temp_2,"F in celsius is",cel,"C")
      elif choice ==3:
          break
      else:
          print("invalid entry")



