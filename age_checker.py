#age_checker.py

your_age = input("your age?")
friends_age = input("friends age?")

if int(your_age) >= 18 or int(friends_age) >= 18:
    print ("congrats, one of you is old enough to vote")
else:
    print("Sorry, neither can vote")
