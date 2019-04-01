#if else chain

#Get user balance
balance = input("Enter balance: ")

if int(balance) <= 0:
    print("Would you like to make a deposit?")
elif int(balance) <= 50:
    print("No interest!")
elif int(balance) <100:
    print("Interest rate is 1%")
else:
    print("Your interest rate is 2%")
