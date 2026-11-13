import pytest
from matches_retriever.data_processing import _format_name

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