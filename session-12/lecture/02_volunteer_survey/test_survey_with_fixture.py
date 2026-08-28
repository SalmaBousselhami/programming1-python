import pytest
from red_cross_survey import VolunteerSurvey

# Define the fixture
@pytest.fixture
def volunteer_survey():
    """Create a survey instance for all tests."""
    question = "What humanitarian region do you work in?"
    survey = VolunteerSurvey(question)
    return survey

# Use the fixture in tests
def test_store_single_response(volunteer_survey):
    """Test storing a single response."""
    volunteer_survey.store_response('Africa')
    assert 'Africa' in volunteer_survey.responses

def test_store_empty_response(volunteer_survey):
    """Test that storing an empty response raises a ValueError."""
    # Attempt to store an empty response
    with pytest.raises(ValueError):
        volunteer_survey.store_response('')

def test_store_three_responses(volunteer_survey):
    """Test storing multiple responses."""
    responses = ['Southeast Asia', 'Middle East', 'Africa']
    for response in responses:
        volunteer_survey.store_response(response)
    
    for response in responses:
        assert response in volunteer_survey.responses