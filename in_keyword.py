#in_keyword

# Names registered
registered_names = ['tony', 'bob', 'mary', 'john', 'roger']

username = input("Please enter desired user name: ")

#Check if variable is in list
if username in registered_names:
    print("Sorry, taken")
else:
    print("This is available")


#Check is value is NOT in list
if username not in registered_names:
    print("This is available")
else:
    print("Sorry, taken")
    
