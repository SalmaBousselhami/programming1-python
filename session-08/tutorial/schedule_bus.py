def schedule_bus():
    """Schedule a bus trip for the Freedom Riders."""
    print(f"Busing to: {destination}")
    print(f"Capacity: {bus_seats} seats")
    print(f"Mandatory Protocol: {training_focus}")
    print("---------------------------------")

# 1. Using a Positional Argument (Uses all defaults)
schedule_bus("Jackson")

# 2. Overriding a Default (Changing the bus size)
schedule_bus("Nashville", 45)

# 3. Using Keyword Arguments (Order doesn't matter here!)
schedule_bus(training_focus="Voter Registration Training", destination="Anniston")