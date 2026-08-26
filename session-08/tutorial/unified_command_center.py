resources = {}
speakers = []

# --- Add function definition for add_to_march_plan ---
pass

# --- function definition for the output ---
def build_march_plan(speakers, resources):
    print("--- 📢 OFFICIAL MARCH ON WASHINGTON PROGRAM 📢 ---")
       
    print("\nOrder of Events:")
    for speaker in speakers:
        print(f"  - Speech by: {speaker}")
    
    print("\nLogistics Checklist:")
    for item, quantity in resources.items():
        print(f"  - {item.replace('_', ' ').title()}: {quantity}")


# --- Add speakers and logistics ---
pass

# --- Call the function ---
build_march_plan(speakers, resources)