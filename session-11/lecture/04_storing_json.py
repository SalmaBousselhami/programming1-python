import json

# Example: Convert an ExpenseReport to a dictionary
report_data = {
    "person": "Dr. Dietrich Bonhoeffer",
    "destination": "Munich",
    "stated_total": 60.70,
    "reason": "Ecumenical discussions with German church leaders",
    "items": [
        {"category": "train", "amount": 15.50, "description": "Berlin to Munich"},
        {"category": "hotel", "amount": 25.00, "description": "Two nights accommodation"},
        {"category": "meals", "amount": 12.20, "description": "Meals during stay"},
        {"category": "taxi", "amount": 3.0, "description": "Airport transfers"}
    ]
}

# Serialize to JSON
json_string = json.dumps(report_data)
print("Serialized Report:")
print(json_string)

# Save to file
from pathlib import Path
path = Path(__file__).parent / 'bonhoeffer_report.json'
path.write_text(json_string)
print(f"\nSaved to {path}")