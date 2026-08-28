# 1. Setup Data
item_name = "Blueberry Muffin"
item_price = 3.50
quantity = 4

# 2. Math Operations
subtotal = item_price * quantity
tax = subtotal * 0.07
grand_total = subtotal + tax

# 3. String & Print Operations
divider = "-" * 25
print(divider)
print("CUSTOMER RECEIPT")
print(divider)
print("Item:", item_name) # Option 1: Using a comma to separate the string and variable (it will automatically add a space)
print("Quantity: " + str(quantity)) # Option 2: Concatenating strings, but we need to convert (cast) quantity to a string first
print(f"Subtotal: ${subtotal}") # Option 3: Using an f-string for cleaner formatting
print(f"Tax: ${tax}")
print(f"Total: ${grand_total}") 
print(divider)