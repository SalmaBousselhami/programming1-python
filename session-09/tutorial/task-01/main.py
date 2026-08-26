from lion import Lion
from den import Den

# --- Simulation ---

# 1. Create Lions
leo = Lion("Leo", 9, 88)
leo.set_hunger(7)
sultan = Lion("Sultan", 8, 23)
sultan.set_hunger(4)

# 2. Setup the Den
babylon_den = Den()
babylon_den.open()
babylon_den.add_lion(leo)
babylon_den.add_lion(sultan)

# 3. Get the report
report = babylon_den.get_hunger_report()
babylon_den.close()

if report:
    print(f"--- Royal Den Report (539 BCE) 🏛️ ---")
    print(f"Lions in Den: {report['lion_count']}")
    print(f"Average Hunger Level: {report['average_hunger']}/10")