import pytest
from matches_retriever.data_processing import _calculate_age_years

def test_calculate_age_years_returns_correct_age():
	match_date = "20000101"
	date_of_birth = "19800101"
	expected_years = 20

	calculated_years = _calculate_age_years(match_date, date_of_birth)
	assert pytest.approx(calculated_years, rel=0.5) == expected_years
