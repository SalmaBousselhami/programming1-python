import json
from pathlib import Path

# Load JSON from file
path = Path(__file__).parent / 'bonhoeffer_report.json'
contents = path.read_text()
report_data = json.loads(contents)

# Display loaded data
print("Loaded Report:")
print(f"Traveler: {report_data['person']}")
print(f"Destination: {report_data['destination']}")
print(f"Purpose: {report_data['reason']}")
print(f"\nExpense Items:")
for item in report_data['items']:
    print(f"  - {item['category']}: ${item['amount']:.2f} ({item['description']})")
print(f"\nStated Total: ${report_data['stated_total']:.2f}")