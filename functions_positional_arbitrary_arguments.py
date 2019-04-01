#functions_positional_arbitrary_arguments.py
#pos. and arbitrary arguments together

def assign_seat(seat, *requests):
	"""Assign a seat and requests to a passenger"""
	print("\nAssign seat number " + str(seat) + " the following requests")
	for request in requests:
		print("- " + request)

assign_seat(36, 'window seat')