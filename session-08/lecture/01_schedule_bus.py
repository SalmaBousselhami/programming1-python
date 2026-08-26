def schedule_bus(
    destination, bus_seats=20, 
    training_focus="Non-violent Resistance", coordinator=""
    ):
    """Schedule a bus trip for the Freedom Riders."""

    print(f"Busing to: {destination}")
    print(f"Capacity: {bus_seats} seats")
    print(f"Mandatory Protocol: {training_focus}")

    if coordinator:
        print(f"Coordinator: {coordinator}")

    print("---------------------------------")

schedule_bus("Jackson")
schedule_bus("Nashville", coordinator="Ella Baker")