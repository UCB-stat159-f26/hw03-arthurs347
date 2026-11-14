import numpy as np
from datetime import datetime
from .data_fetching import _get_career_stats, _get_player_dob, _format_name

def get_plotting_data(name):
	"""Returns processed data to reproduce plot as a pandas dataframe"""
	raw_career_stats = _get_career_stats(name)
	cleaned_data = _clean_data_for_processing(raw_career_stats)

	match_dates = cleaned_data['Date']	
	primary_player_dob = _get_player_dob(name)
	opponents_dobs_or_age = cleaned_data["Opponent_DOB_Or_Age"]

	# Extract age in years for primary player and opponents
	primary_player_age_years = _calc_primary_player_ages(match_dates, primary_player_dob)
	opponent_ages_years = _handle_opponent_ages(match_dates, opponents_dobs_or_age)
	
	# Calculate difference in years between primary player and their opponent's ages per match
	opponent_years_diff = primary_player_age_years - opponent_ages_years
	
	# Tidy up table to contain the primary player's age and the difference in years between their opponents
	cleaned_data['Primary_Player_Age'] = primary_player_age_years
	cleaned_data['Opponent_Years_Diff'] = opponent_years_diff
	
	processed_data = cleaned_data.drop(columns=['Opponent_DOB_Or_Age'])

	data_with_attrs = _add_attrs(processed_data, name)
	
	return data_with_attrs

def _add_attrs(df, name):
	"""Add attributes to dataframe useful for plotting graph"""
	df.attrs['fullname'] = _format_name(name)
	df.attrs['minage'] = int(min(df['Primary_Player_Age']))
	df.attrs['maxage'] = int(max(df['Primary_Player_Age']))

	return df
	
def _handle_opponent_ages(match_dates, opponent_dobs_or_age):
	"""Handle and return opponent ages if input is dob's or actual ages (in years)"""
	# Check if values are formatted as dobs or ages
	try:
		# Case of values formatted as dobs by checking first value type
		datetime.strptime(opponent_dobs_or_age[0], "%Y%m%d")
		opponent_ages = _calc_opponent_ages(match_dates, opponent_dobs_or_age)
		print("String")
	except ValueError:
		# Case of values formatted as years
		print("Years")
		opponent_ages = opponent_dobs_or_age.astype('float')
		
	return opponent_ages
	
def _clean_data_for_processing(raw_data):
	"""Return cleaned df with only necessary data"""
	data_renamed = raw_data.rename(columns={0: 'Date', 1: 'Tournament', 4: 'Match_Outcome_Player', 
											11: 'Opponent_Name', 16: 'Opponent_DOB_Or_Age'
										   })
	data_extracted = data_renamed[['Date', 'Tournament', 'Match_Outcome_Player', 
								   'Opponent_Name', 'Opponent_DOB_Or_Age']]

	# Convert columns to strings for easier processing
	data_extracted['Date'] = data_extracted['Date'].astype('str')
	data_extracted['Opponent_DOB_Or_Age'] = data_extracted['Opponent_DOB_Or_Age'].astype('str')

	return data_extracted
	

def _calc_primary_player_ages(match_dates, player_dob):
	"""Return the primary player's ages in years for all matches as a numpy array"""
	player_age_years = np.array([])
	
	for match_date in match_dates:
	    player_age = _calculate_age_years(match_date, player_dob)
	    player_age_years = np.append(player_age_years, player_age)

	return player_age_years

def _calc_opponent_ages(match_dates, opponent_dobs):
	"""Return opponent's ages in years for all matches as a numpy array"""
	opponents_age_years = np.array([])

	for match_date, opponent_dob in zip(match_dates, opponent_dobs):
		opponent_age = _calculate_age_years(match_date, opponent_dob)
		opponents_age_years = np.append(opponents_age_years, opponent_age)

	return opponents_age_years

def _calculate_age_years(match_date, date_of_birth):
	"""Return age in years for provided match date and player date of birth"""
	date_parsed = datetime.strptime(match_date, "%Y%m%d")
	dob_parsed = datetime.strptime(date_of_birth, "%Y%m%d")
	
	days_diff = (date_parsed - dob_parsed).days
	age_years = days_diff / 365
	
	return age_years