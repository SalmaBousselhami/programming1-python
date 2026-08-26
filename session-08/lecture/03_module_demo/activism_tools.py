def organize_march(size, *supporters):
    """Summarize the march we are about to organize."""
    print(f"\nOrganizing a march with {size} expected participants")
    print("Speakers:")
    for supporter in supporters:
        print(f"- {supporter}")


def plan_logistics(location, **resources):
    """Plan logistics for an event."""
    print(f"\nPlanning logistics for {location}")
    print("Resources needed:")
    for resource, quantity in resources.items():
        print(f"- {quantity} {resource.replace('_', ' ')}")

def coordinate_speakers(*speakers):
    pass