import time

# Get current time
current_time = time.time()
print(f"Current time (seconds since epoch): {current_time}")

# Format current date and time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted time: {formatted_time}")

# Create a delay (sleep for 1 second)
print("Daniel enters the den...")

for s in range(4):
    time.sleep(1)
    print("...")

print("The lions are peaceful.")