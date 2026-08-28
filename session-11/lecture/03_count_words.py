from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
        # pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


# Analyze multiple files, assuming 'trip_copenhagen.txt' is missing
filenames = ['trip_stockholm.txt', 'trip_munich.txt']
# filenames = ['trip_stockholm.txt', 'trip_munich.txt', 'trip_copenhagen.txt']

for filename in filenames:
    path = Path(__file__).parent / 'travel_expense_reports' / filename
    count_words(path)