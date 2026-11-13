import pytest
import numpy as np
import pandas as pd
import json
from matches_retriever.data_processing import (
	_handle_opponent_ages,
	_clean_data_for_processing,
	_calc_primary_player_ages,
	_calc_opponent_ages, 
	_calculate_age_years
)

female_player_career = [
	["19951030", "Canadian Open", "Carpet", "W", "L", "", "", "WC", "Q1", "6-1 6-1", "3",
	 "Anne Miller", "149", "7", "", "R", "19770119", "", "USA", "0", "", "", "", "", "", "", "1995-W-WT-CAN-02A-1995-013"],
	
	["19970307", "Indian Wells", "Hard", "W", "L", "", "", "WC", "Q1", "6-4 6-0", "3",
	 "Alexia Dechaume Balleret", "87", "", "", "R", "19700503", "", "FRA", "0", "", "", "", "", "", "", "1997-W-WT-USA-02A-1997-006"],
	
	["19970804", "Manhattan Beach", "Hard", "W", "L", "", "", "WC", "Q3", "7-6 4-6 6-3", "3",
	 "Magui Serna", "54", "6", "", "L", "19790301", "167", "ESP", "0", "", "", "", "", "", "", "1997-W-WT-USA-07A-1997-026"]
]

male_player_career = [
	["20010910", "Spain F10", "Hard", "S", "L", "", "", "WC", "R32", "2-6 7-5 6-2", "3", 
	 "Guillermo Platel", "731", "", "", "R", "22.264202601", "", "ESP", "0",
	 "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
	 "2001-M-FU-ESP-10A-2001-002", "", "1", "1"],
	
	["20010917", "Seville CH", "Clay", "C", "L", "", "", "WC", "R16", "3-6 6-1 6-3", "3",
	 "Stefano Galvani", "161", "2", "", "R", "24.2902121834", "178", "ITA", "0",
	 "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "2", "", "", "",
	 "2001-784-024", "", "2", "2"],
	["20010917", "Seville CH", "Clay", "C", "W", "", "", "WC", "R32", "6-4 6-4", "3",
   "Israel Matos Gil", "751", "", "Q", "U", "18.7597535934", "", "ESP", "0", 
	 "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
	 "2001-784-015", "", "1", "1"]
]

def test_handle_opponent_ages_handles_dobs_and_ages():
	match_dates = np.array(["20000101", "20010101"])
	opponent_dobs = np.array(["19800101", "19810101"])
	opponent_years = np.array([20, 20])

	handled_opponent_dobs = _handle_opponent_ages(match_dates, opponent_dobs)
	handled_opponent_years = _handle_opponent_ages(match_dates, opponent_years)
	
	expected_years = np.array([20, 20])

	assert handled_opponent_dobs == pytest.approx(expected_years, abs=0.5)
	assert handled_opponent_years == pytest.approx(expected_years, abs=0.5)

def test_clean_data_for_processing():
	raw_df_female = pd.DataFrame(female_player_career)
	raw_df_male = pd.DataFrame(male_player_career)

	cleaned_df_female = _clean_data_for_processing(raw_df_female)
	cleaned_df_male = _clean_data_for_processing(raw_df_male)

	expected_columns = ['Date', 'Tournament', 'Match_Outcome_Player', 
								   'Opponent_Name', 'Opponent_DOB_Or_Age']
	expected_row_num = 3
	expected_date_type = 'str'
	expected_opp_dob_age_type = 'str'

	assert list(cleaned_df_female.columns) == expected_columns
	assert list(cleaned_df_male.columns) == expected_columns

	assert len(cleaned_df_female) == expected_row_num
	assert len(cleaned_df_male) == expected_row_num

	assert cleaned_df_female['Date'].dtype == expected_date_type
	assert cleaned_df_male['Date'].dtype == expected_date_type

	assert cleaned_df_female['Opponent_DOB_Or_Age'].dtype == expected_opp_dob_age_type
	assert cleaned_df_male['Opponent_DOB_Or_Age'].dtype == expected_opp_dob_age_type
	
def test_calc_primary_player_ages_returns_correct_ages():
	match_dates = np.array(["20000101", "20010101"])
	player_dob = "19800101"
	expected_years = np.array([20, 21])

	calculated_years = _calc_primary_player_ages(match_dates, player_dob)
	assert calculated_years == pytest.approx(expected_years, abs=0.5)

def test_calc_opponent_ages_returns_correct_ages():
	match_dates = np.array(["20000101", "20010101"])
	opponent_dobs = np.array(["19800101", "19810101"])
	expected_years = np.array([20, 20])

	calculated_years = _calc_opponent_ages(match_dates, opponent_dobs)
	assert calculated_years == pytest.approx(expected_years, abs=0.5)
	
def test_calculate_age_years_returns_correct_age():
	match_date = "20000101"
	date_of_birth = "19800101"
	expected_years = 20

	calculated_years = _calculate_age_years(match_date, date_of_birth)
	assert pytest.approx(calculated_years, abs=0.5) == expected_years
