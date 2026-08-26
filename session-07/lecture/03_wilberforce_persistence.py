prompt = "\nWilberforce has tried {} time(s) to convince the parliament..."
prompt += "\nEnter 'give_up' if he gives up, or anything else to continue the fight: "
message = ""
attempts = 0

while message != 'give_up':
    message = input(prompt.format(attempts))

    attempts += 1
    
    if message != 'give_up':
        print(f"Attempt {attempts}: Wilberforce speaks passionately against slavery!")

        if attempts >= 5:  # Simulate the Slave Trade Act passing after many attempts (actually there have been more than 12 major attempts)
            print("After relentless efforts, the Slave Trade Act of 1807 is passed!")
            break
        else:
            print("The parlament rejects the proposal.")
    else:
        print("Wilberforce has given up the fight.")

print(f"Total attempts in Parliament: {attempts}")