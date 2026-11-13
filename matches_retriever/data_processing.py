from datetime import datetime

def process_data_for_plot():
	"""Returns processed data to reproduce plot as a pandas dataframe"""
	
	return NotImplementedError("process_data_for_plot not implemented")

def _calculate_age_years(match_date, date_of_birth):
	"""Return age in years for provided match data and player date of birth"""
	date_parsed = datetime.strptime(match_date, "%Y%m%d")
	dob_parsed = datetime.strptime(date_of_birth, "%Y%m%d")
	
	days_diff = (date_parsed - dob_parsed).days
	age_years = days_diff / 365
	
	return age_years