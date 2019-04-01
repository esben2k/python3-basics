#functions_return_value.py

def formatted_name(first_name, last_name):
	"""return formatted name"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

teacher = formatted_name('esben', 'hansen')
print(teacher)

def get_formatted_username(email_address):
	"""Return formatted username"""
	username = email_address.strip()
	return username

user = get_formatted_username("esben@example.com               ")
print(user)