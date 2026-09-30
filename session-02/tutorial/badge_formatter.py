first_name = "  ada"
last_name = "LOVELACE  "
role = "  speaker"
workshop = "python for beginners"




#first_name = "  grace  "
#last_name = "hopper"
#role = "developer  "
#workshop = "  debugging legacy code  "

first_name = first_name.strip()
last_name = last_name.strip()
role = role.strip().upper()
workshop = workshop.strip().title()
badge_name = f"{first_name.upper()} {last_name.upper()}" 
badge_id = first_name.lower() +"."+  last_name.lower()


print(f'{badge_name}\n{role} | {workshop}\nBadge ID: {badge_id}')
