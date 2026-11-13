import requests

def get_career_stats(name):
    """Return the careers stats for a given player"""
	url = _get_url_from_name(name)
	raise NotImplementedError("get_career_stats not implemented")

def _get_url_from_name(name):
	"""Create tennisabstract career url from name"""
	formatted_name = _format_name(name)
	formated_url = f"https://www.tennisabstract.com/jsmatches/{formatted_name}Career.js"

	# Check if player exists
	response = requests.get(formated_url)
	status_code = response.status_code

	if (status_code == 404):
		raise ValueError("Player not found")
		
	return formated_url


def _format_name(name):
	"""Returns player name as formatted in tennisabstract url"""
	#TODO: Reduce to under 10 lines
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