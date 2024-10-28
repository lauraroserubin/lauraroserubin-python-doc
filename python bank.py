'''
Author:Laura Rose Rubin
Date:28-10-2024
Description:Write a program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to:
    Check Balance
    Deposit Money
    Withdraw Money
    Exit
'''



balance_amount=1000
while True:
    print("1.\tCheck balance")
    print("2.\tDeposit money")
    print("3.\tWithdraw money")
    print("4.\tExit")
    choice= int(input("enter your choice:"))
    if choice ==1:
        print(f"the current balance ${balance_amount}")
    elif choice ==2:
        deposit_amount = float(input("enter the amount"))
        balance_amount = balance_amount +deposit_amount
        print(f"the deposit amount ${deposit_amount}and"f"the current balance ${balance_amount}")
    elif choice ==3:
        withdraw_amount = float(input("enter the amount to withdraw"))
        balance_amount = balance_amount-withdraw_amount
        if withdraw_amount > balance_amount:
            print(f" balance is insufficient")
        else:
            print(f"the amount withdrawn from the account and"f"${withdraw_amount} the balance amount and"f"${balance_amount}")
    elif choice ==4:
        break
    else:
        print("invalid entry")

