guide_sightings = ['kingfisher', 'fish eagle', 'ibis']

# Copy by using slicing
my_sightings = guide_sightings[:]

# This DOES NOT make a copy; it creates a second name for the same list
# my_sightings = guide_sightings (uncomment to test)

# Add a unique sighting to the guide's list
guide_sightings.append('shoebill')

# Add a unique sighting to our own list
my_sightings.append('pelican')

print("The guide's updated sightings (includes shoebill):")
print(guide_sightings)

print("\nMy personal updated sightings (includes pelican):")
print(my_sightings)