#functions_arbitrary_arguments2.py


#the asterisk tells python to create an empty TUPLE called requests
def create_passenger(*requests):
	"""Print user requests"""
	print("\nThis passenger has requested: ")
	for request in requests:
		print("- " + request)


create_passenger('isle seat', 'seat near front', 'pre-orderbreakfast')
