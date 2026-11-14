import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

def get_career_stats(name):
	"""Return the careers stats for a given player as a pandas dataframe"""
	url = _get_url_from_name(name)

	response = requests.get(url)
	json_parsed = _format_response_to_json(response)

	# Convert json to pandas dataframe
	career_stats = pd.DataFrame(json_parsed)
	
	return career_stats

def _get_abstract_page(name):
	"""Return the abstract page for a player as html"""
	formatted_name = _format_name(name)
	formatted_url = f"https://www.tennisabstract.com/cgi-bin/wplayer-classic.cgi?p={formatted_name}"

	response = requests.get(formatted_url)
	html = response.text
	return html
	
def _format_response_to_json(response):
	"""Format response object to json"""
	javascript_text = response.text

	# Obtain beginning and end indexes of the list
	text_split_start = javascript_text.find('[')
	text_split_end = javascript_text.rfind(']')+1

	# Extract and parse text to json
	json_indexed = javascript_text[text_split_start:text_split_end]
	json_parsed = json.loads(json_indexed)
	
	return json_parsed

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

def _extract_names(name):
	formatted_name = _format_name(name)
	split_name = re.findall(r'[A-Z][a-z]*', formatted_name)

	first_name = split_name[0]
	last_name = split_name[1]
	return first_name, last_name

def _format_name(name):
	"""Return player name as formatted in tennisabstract url"""
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

def _get_player_dob(name):
	"Return the date of birth of a player"
	abstract_page = _get_abstract_page(name)
	soup = BeautifulSoup(abstract_page, "html.parser")

	age_text = soup.find("td", string=re.compile("Age:")).get_text()
	dob = re.search(r"\((.*?)\)", age_text).group(1)

	return dob