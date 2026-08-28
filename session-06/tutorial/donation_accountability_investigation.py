# Donation records - what donors intended their money to be used for
donations = {
    'American Red Cross': 'Medical supplies for the clinic',
    'UNICEF': 'Food for children',
    'World Health Org': 'Medical supplies for the clinic',
    'Catholic Charities': 'Food for children',
    'Oxfam': 'Educational programs',
    'Save the Children': 'Educational programs',
    'Global Fund': 'Medical supplies for the clinic',
}

# Actual use - where the money really went
actual_use = {
    'American Red Cross': 'Medical supplies for the clinic',
    'UNICEF': 'Administrative overhead',
    'World Health Org': 'Medical supplies for the clinic',
    'Catholic Charities': 'Food for children',
    'Oxfam': 'Administrative overhead',
    'Save the Children': 'Educational programs',
    'Global Fund': 'Building renovation project',
}

# 1. Loop through donors and print their intended donations
print("=" * 60)
print("DONATION INTENTIONS:")
print("=" * 60)


# TODO: Add your code here

# 2. Check for misuse - compare intended vs actual
print("\n" + "=" * 60)
print("MISUSE DETECTION:")
print("=" * 60)

# TODO: Add your code here

# 3. Find ALL purposes that were misused (using set())
print("\n" + "=" * 60)
print("PURPOSES WITH MISUSE:")
print("=" * 60)

# Get all purposes that were misused (intended but not matched actual)

# TODO: Add your code here

# Show unique misused purposes
print("Purposes that were misused:")

# TODO: Add your code here

# 4. Show unique purposes intended vs actual
print("\n" + "=" * 60)
print("SUMMARY - UNIQUE PURPOSES:")
print("=" * 60)

# TODO: Add your code here

# Additional analysis: How many donors were affected by misuse?
print("\n" + "=" * 60)
print("IMPACT SUMMARY:")
print("=" * 60)

# TODO: Add your code here