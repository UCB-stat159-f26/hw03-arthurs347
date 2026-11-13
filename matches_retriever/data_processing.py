def get_career_stats(name):
	"""Return the careers stats for a given player"""
	url = _get_url_from_name(name)
	raise NotImplementedError("get_career_stats not implemented")

# Final format FirstnameLastnameCareer.js
def _get_url_from_name(name):
	"""Create tennisabstract career url from name"""
	formatted_name = _format_name(name)
		
	formated_url = f"https://www.tennisabstract.com/jsmatches/{first_name_capitalized}{last_name_capitalized}Career.js"

	#TODO: Check if player exists
	
	raise NotImplementedError("_get_url_from_name not implemented")


def _format_name(name):
	"""Returns player name as formatted in tennisabstract url"""
		# Split provided name string based on provided format
	if (" " in name):
		split_name = name.split()
	else:
		return name
	
	# Extract First & Last Name & capitalize
	first_name = split_name[0]
	first_name_capitalized = first_name.capitalize()
	
	last_name = split_name[1]
	last_name_capitalized = last_name.capitalize()

	return f"{first_name_capitalized}{last_name_capitalized}"