#funtions_arbitrary_keyword_arguments.py

def seat_profile(first, last, **passenger_info):
	"""Build dictionary containing all passenger information"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in passenger_info.items():
		profile[key] = value
	return profile

passenger_profile = seat_profile('esben','hansen',seat_number=36, breakfast_ordered="yes")

print(passenger_profile)