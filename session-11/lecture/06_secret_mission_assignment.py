"""
Secret mission assignment system for trusted contacts of the Resistance Circle. 
"""

from pathlib import Path
import json

name = input("What is your name? ")
name_file =   name.lower().replace(" ", "_") # Normalize name for filename

path = Path(__file__).parent / "trusted_contacts" / f'{name_file}_trusted_contact.json'

if path.exists():
    contents = path.read_text()
    contact = json.loads(contents)
    location = input(f"Greetings, {contact['name']}! Where are you from? ")

    if location.lower() == contact['location'].lower():
        print("Perfect. We trust you with this mission.")
    else:
        print("Allright. Do you want to buy some potatoes?")
else:
    sendor = input("Nice to meet you. Who recommended my potatoes to you? ")
    sendor_file = sendor.lower().replace(" ", "_")

    path_sendor = Path(__file__).parent / "trusted_contacts" / f'{sendor_file}_trusted_contact.json'

    if path_sendor.exists():
        print(f"Perfect. We trust you with this mission.")

        print(f"We'll remember you for future communications.")
        location = input(f"Where are you from? ")
        contact = {"name": name, "location": location}
        contents = json.dumps(contact, indent=2)
        path.write_text(contents) 
    else:
        print(f"Allright. Do you want to buy some potatoes?")