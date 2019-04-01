#dictionary_user_input.py
# Adding user input to a dictionary

# Create empty dict
rental_properties = {}

# Set a flag to indicate we are taking applications
rental_open = True

while rental_open:
	#prompt users name and address
	username = input("\nWhat is your name? ")
	rental_property = input("Waht is the address? ")

	#store responses in dictionary
	rental_properties[username] = rental_property

	#ask if the user knows anyone else looking to rent a property
	repeat = input("\nDo you know anyone who might like to rent out their property? ")
	if repeat =="no":
		rental_open = False

	# adding properties is complete

print("\n--- Property to rent ---")
for username, rental_property in rental_properties.items():
	print(username + " has " + rental_property + " to rent.")