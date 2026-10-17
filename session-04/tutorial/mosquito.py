import random

number_of_mosquitoes = 100
number_of_waterholes = 10
breed_rate = 1.2
kill_rate = 0.2
waterhole_destroy_rate = 0.5
new_waterholes_per_rain_event = 3
rain_event_probability = 0.6

history = []
max_mosquitoes = number_of_mosquitoes
max_waterholes = number_of_waterholes

for day in range(1, 357):
    if random.random() < rain_event_probability:
        number_of_waterholes += new_waterholes_per_rain_event

    number_of_waterholes = int(
        number_of_waterholes * (1 - waterhole_destroy_rate)
    )

    number_of_mosquitoes = int(
        number_of_mosquitoes * (breed_rate ** number_of_waterholes)
    )

    number_of_mosquitoes = int(
        number_of_mosquitoes * (1 - kill_rate)
    )

    history.append((day, number_of_mosquitoes, number_of_waterholes))

    if number_of_mosquitoes > max_mosquitoes:
        max_mosquitoes = number_of_mosquitoes

    if number_of_waterholes > max_waterholes:
        max_waterholes = number_of_waterholes

    print(
        f"Day {day}: Mosquitoes: {number_of_mosquitoes}, "
        f"Waterholes: {number_of_waterholes}"
    )

print(f"\nHighest mosquito count: {max_mosquitoes}")
print(f"Highest number of waterholes: {max_waterholes}")