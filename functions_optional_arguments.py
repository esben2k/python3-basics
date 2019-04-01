#functions_optional_arguments.py

#assigning an empty string to optional argument.
def formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name"""
	if middle_name:
		full_name= first_name + " " + middle_name + " " + last_name
	else:
		full_name= first_name + " " + last_name
	return full_name.title()

teacher = formatted_name('esben','hansen','nme')
print(teacher)
teacher = formatted_name('esben','hansen')
print(teacher)