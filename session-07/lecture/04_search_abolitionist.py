abolitionists = ['Thomas Clarkson', 'Harriet Beecher', 
                 'Olaudah Equiano', 'William Wilberforce']

searching_for = 'William Wilberforce'

while True:  # Loop "forever"
    if not abolitionists:
        print(f"Abolitionist not found in records.")
        break
    
    person = abolitionists.pop(0)
    print(f"Checking: {person}")
    
    if person == searching_for:
        print(f"✓ Found: {person}!")
        break