#functions_modifying_a_list.py
#airline check-in program

def passengers(not_checked_in, checked_in):
	"""Simulate passengers not checked in"""
	while not_checked_in:
		#pop each passenger out from the list
		current_passenger = not_checked_in.pop()

		print("Checking in passenger. " + current_passenger)
		checked_in.append(current_passenger)

def show_checked_in_passengers(checked_in):
	"""Show all checked-in passengers"""
	print("\nThe following passengers have been checked in.")
	for passengers in checked_in:
		print(passengers)

not_checked_in = ['Esben Hansen', 'John Doe', 'Still Well', 'Silent Singer']
checked_in = []

#to prevent modifying the list passed to the function, use a copy like below:
passengers(not_checked_in[:], checked_in)

#the list will be modified when passed like below
passengers(not_checked_in, checked_in)
show_checked_in_passengers(checked_in)

