volunteers = [
    {
        'name': 'Sister Agnes', 
        'center': 'Home for the Dying Destitute', 
        'years_served': 12, 
        'spirituality_score': 95, 
        'community_impact': 'Training new volunteers', 
        'passport': 'ALB-123456'
    },
    {
        'name': 'Brother John', 
        'center': 'Children\'s Home', 
        'years_served': 8, 
        'spirituality_score': 88, 
        'community_impact': 'Healthcare initiatives', 
        'passport': 'IND-789012'
    },
    {
        'name': 'Sister Mary', 
        'center': 'Leprosy Center', 
        'years_served': 15, 
        'spirituality_score': 98, 
        'community_impact': 'Medical care and dignity programs', 
        'passport': 'IND-345678'
    },
    {
        'name': 'Brother Paul', 
        'center': 'Home for the Unwanted Children', 
        'years_served': 6, 
        'spirituality_score': 82, 
        'community_impact': 'Educational programs', 
        'passport': 'IND-901234'
    },
    {
        'name': 'Sister Catherine', 
        'center': 'Mobile Clinic', 
        'years_served': 10, 
        'spirituality_score': 91, 
        'community_impact': 'Emergency medical response', 
        'passport': 'IND-567890'
    },
]

flights = {
    'outbound': {
        'flight_number': 'AA-1001', 
        'route': 'Kolkata (CCU) to Washington D.C. (IAD)', 
        'date': 'February 3, 1985', 
        'departure_time': '14:30', 
        'arrival_time': '23:45 (next day)', 
        'duration': '16 hours 45 minutes', 
        'aircraft': 'Boeing 747', 
        'airline': 'American Airlines', 
        'available_seats': ['1A', '1B', '1C', '1D'],
        'passengers': []
    },
    'return': {
        'flight_number': 'AA-1002', 
        'route': 'Washington D.C. (IAD) to Kolkata (CCU)', 
        'date': 'February 10, 1985', 
        'departure_time': '10:00', 
        'arrival_time': '20:15 (next day)', 
        'duration': '17 hours 15 minutes', 
        'aircraft': 'Boeing 747', 
        'airline': 'American Airlines', 
        'available_seats': ['2A', '2B', '2C', '2D'],
        'passengers': []
    }
}

# Step 1: Calculate dedication score for each volunteer and update their records
print("=" * 70)
print("VOLUNTEER EVALUATION FOR MEDAL CEREMONY")
print("=" * 70)

# TODO: Add your code here

# Step 2: Select the 3 best volunteers
print("\n" + "=" * 70)
print("SELECTING TOP 3 VOLUNTEERS")
print("=" * 70)

top_3_volunteers = []

# TODO: Add your code here

print("\n✓ TOP 3 SELECTED VOLUNTEERS:")
for i, volunteer in enumerate(top_3_volunteers, 1):
    print(f"\n{i}. {volunteer['name']}")
    print(f"   Score: {volunteer.get('dedication_score', 0.0):.1f}")
    print(f"   Center: {volunteer['center']}")
    print(f"   Impact: {volunteer['community_impact']}")

# Step 3: Create complete travel roster, add the three volunteers to the travel roster along with Mother Teresa, and assign them to the flights
print("\n" + "=" * 70)
print("OFFICIAL TRAVEL ROSTER - PRESIDENTIAL MEDAL CEREMONY")
print("=" * 70)

travel_roster = {
    'ceremony': {
        'honoree': 'Mother Teresa of Calcutta',
        'award': 'Presidential Medal of Freedom',
        'date': 'February 5, 1985',
        'location': 'The White House, Washington, D.C.',
        'presenter': 'President Ronald Reagan',
        'citation': 'In recognition of her significant contributions to humanitarian relief'
    },
    'travelers': [
        {'name': 'Mother Teresa', 'position': 'Founder, Missionaries of Charity', 'passport': 'ALB-000001'}
    ]
}

# TODO: Add you code here

# Step 4: Add passengers to outbound and return fligt passenger lists
# - Assign each one of the available seats
# - Add them as dicts with the keys 'name', 'passport', 'seat'

# TODO: Add your code here

# Step 5: Generate travel manifest
print("\n📋 CEREMONY INFORMATION:")
print(f"  Honoree: {travel_roster['ceremony']['honoree']}")
print(f"  Award: {travel_roster['ceremony']['award']}")
print(f"  Date: {travel_roster['ceremony']['date']}")
print(f"  Location: {travel_roster['ceremony']['location']}")
print(f"  Presenter: {travel_roster['ceremony']['presenter']}")

print("\n✈️  OUTBOUND FLIGHT - KOLKATA TO WASHINGTON D.C.")
print(f"  Flight: {flights['outbound']['flight_number']} | Date: {flights['outbound']['date']}")
print(f"  Route: {flights['outbound']['route']}")
print(f"  Departure: {flights['outbound']['departure_time']} | Arrival: {flights['outbound']['arrival_time']}")

print("\n  PASSENGERS:")
for passenger in flights['outbound']['passengers']:
    print(f"    {passenger['name']:30} | Passport: {passenger['passport']:12} | Seat: {passenger['seat']}")

print("\n✈️  RETURN FLIGHT - WASHINGTON D.C. TO KOLKATA")
print(f"  Flight: {flights['return']['flight_number']} | Date: {flights['return']['date']}")
print(f"  Route: {flights['return']['route']}")
print(f"  Departure: {flights['return']['departure_time']} | Arrival: {flights['return']['arrival_time']}")

print("\n  PASSENGERS:")
for passenger in flights['return']['passengers']:
    print(f"    {passenger['name']:30} | Passport: {passenger['passport']:12} | Seat: {passenger['seat']}")

print("\n" + "=" * 70)
print(f"Total Travelers: {len(travel_roster['travelers'])} | Total Flights: 2")
print("✓ ALL BOOKINGS CONFIRMED | ✓ PASSPORTS VERIFIED | ✓ SEATING COMPLETE")
print("\n🎖️  Mother Teresa and her companions are ready for the Medal ceremony!")