#functions_arbitrary_arguments.py


#the asterisk tells python to create an empty TUPLE called requests
def create_passenger(*requests):
	"""Print user requests"""
	print(requests)

create_passenger('isle seat', 'seat near front', 'pre-orderbreakfast')
