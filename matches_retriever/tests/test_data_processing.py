import pytest
import numpy as np
from matches_retriever.data_processing import _calc_primary_player_ages, _calc_opponent_ages, _calculate_age_years

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
