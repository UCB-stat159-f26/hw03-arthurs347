import numpy as np
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def process_data_for_plot():
	"""Returns processed data to reproduce plot as a pandas dataframe"""
	
	return NotImplementedError("process_data_for_plot not implemented")

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