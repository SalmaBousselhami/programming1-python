guests = [
    "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Jack",
    "Karl", "Linda", "Marek", "Nina", "Oscar", "Paul", "Quinn", "Rita", "Steve", "Tariq",
    "Ursula", "Victor", "Wendy", "Xavier", "Yara", "Zane", "Aria", "Ben", "Chloe", "Dan",
    "Spencer", "Peter"
]

# 1. Every 10th guest (Indices 9, 19, 29...)
# Start at 9, no end defined, step of 10
# This is the pythonic way. We have not yet covered this... But be prepared, there is more to come :-)
jubilee_winners = guests[9::10] 
print(f"Jubilee Winners (Voucher): {jubilee_winners}")

# 2. The last 3 guests
late_birds = guests[-3:]
print(f"Late Bird Winners (Taxi): {late_birds}")

# 3. The very last guest
final_guest = guests[-1]
print(f"Special shoutout to {final_guest}, our final guest of the night!")