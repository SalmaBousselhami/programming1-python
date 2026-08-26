responses = {}
polling_active = True
count = 0

print("=== Abolitionist Support Survey ===")
print("Gathering testimonies of support for abolition...\n")

while polling_active and count < 3:  # Limit to 3 for demo
    count += 1
    # Simulating input:
    supporter_responses = [
        ('William Wilberforce', 'God Almighty has set before me two great objects, the suppression of the slave trade and the reformation of manners.'),
        ('Thomas Clarkson', 'Slavery is a moral evil that must cease: Do unto others as you would have them do unto you!'),
        ('Harriet Beecher', 'Every person deserves freedom!')
    ]
    
    name, response = supporter_responses[count - 1]
    responses[name] = response
    print(f"Recorded testimony from {name}")
    
    if count >= 3:
        polling_active = False

# Display results
print("\n=== Recorded Testimonies ===")
for name, testimony in responses.items():
    print(f"\n{name}:")
    print(f"  '{testimony}'")