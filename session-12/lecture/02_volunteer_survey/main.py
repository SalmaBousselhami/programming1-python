from red_cross_survey import VolunteerSurvey

# Create survey
question = "What humanitarian region do you work in?"
survey = VolunteerSurvey(question)

while True:
    # Show question
    survey.show_question()
    
    # Collect response
    response = input("Enter your response (or 'q' to quit): ")
    if response.lower() == 'q':
        break
    
    # Store response
    try:
        survey.store_response(response)
    except ValueError as e:
        print(f"Error: {e}")

# Show results
survey.show_results()