import press_office

# 1. Capture the returned dictionary
dream_speech = press_office.create_press_release(
    "A Historic Day for Justice",
    "I have a dream my four little children will",
    "one day live in a nation where they will not",
    "be judged by the color of their skin but by",
    "content of their character. I have a dream today!",
    attendance=250000, 
    location="Lincoln Memorial", 
    organizer="Bayard Rustin",
    year=1963,
    status="Peaceful",
)

# 2. Print the final result 🖨️
print(f"HEADLINE: {dream_speech['title']}")
print(f"TRANSCRIPT: {dream_speech['content']}")
print(f"EVENT DATA: {dream_speech['metadata']}")

