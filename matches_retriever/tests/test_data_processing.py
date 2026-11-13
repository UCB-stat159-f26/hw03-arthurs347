import pytest
from matches_retriever.data_processing import _get_url_from_name, _format_name

def test_get_url_from_name_handles_invalid_players():
	invalid_name = "Gaston Sanchez"
	
	with pytest.raises(ValueError, match='Player not found'):
	     _get_url_from_name(invalid_name)

def test_get_url_from_name_returns_correct_url():
	expected_url = "https://www.tennisabstract.com/jsmatches/SerenaWilliamsCareer.js"
	name = "Serena Williams"

	created_url = _get_url_from_name(name)

	assert created_url == expected_url
	
def test_format_name_handles_names():
	expected_name = "SerenaWilliams"

	name_lower_spaced = "serena williams"
	name_upper_spaced = "Serena Williams"
	name_upper_concated = "SerenaWilliams"

	formatted_name_lower_spaced = _format_name(name_lower_spaced)
	formatted_name_upper_spaced = _format_name(name_upper_spaced)
	formatted_name_upper_concated = _format_name(name_upper_concated)

	assert formatted_name_lower_spaced == expected_name
	assert formatted_name_upper_spaced == expected_name
	assert formatted_name_upper_concated == expected_name