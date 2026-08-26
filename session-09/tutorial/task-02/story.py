import time
import sys

# Helper function for dramatic effect
def dramatic_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def once_upon_a_time(citizens, babylon_den, haman):

    babylon_den = AngelDen(babylon_den.lions)

    # --- THE STORY BEGINS ---
    dramatic_print("🏛️  WELCOME TO ANCIENT BABYLON, 539 BC...", 0.1)
    time.sleep(1)

    # Minister Haman's persistence
    dramatic_print(f"\n[HAMAN]: 'Your Majesty, King Darius... I have a proposal.'")
    time.sleep(0.5)
    haman.suggest_law("Anyone who prays to any god except the King shall be cast into the Den!")

    count_denials = 0
    while True:
        your_decision_law = input("\n👑 King Darius, do you sign this decree? (y/n): ")

        if your_decision_law.lower() == 'y':
            dramatic_print("✒️  The King presses his signet ring into the wax. The law is irrevocable.")
            break
        else:
            count_denials += 1
            dramatic_print("❌ 'I will not sign this injustice!' you cry.")
            time.sleep(1)
            if count_denials < 3:
                dramatic_print(f"[HAMAN]: 'But Sire, the other ministers insist! It is the will of the people.'")
            else:
                dramatic_print("⚠️  The pressure from the court is becoming unbearable...")
        
            if count_denials >= 5: # Shortened for the task, but kept your logic
                dramatic_print("\n[!] Exhausted, King Darius signs the decree to maintain order.")
                break

    # The Vigilance of the Law
    while citizens:
        citizen = citizens.pop(0)
        time.sleep(1)
        print("\n" + "~" * 40)
        dramatic_print(f"🕵️  The secret police are watching the city...")
        time.sleep(1)
        citizen.pray() # Assuming your Citizen class has this method

        your_decision_den = input(f"\n📢 {citizen.name} has been caught! Throw him to the lions? (y/n/q to quit): ")

        if your_decision_den.lower() == 'y':
            dramatic_print(f"⛓️  Guards seize {citizen.name}. The heavy stone cover of the den is lifted...")
            time.sleep(1.5)
            babylon_den.throw_in(citizen)
        
            # SENSE OF PASSAGE OF TIME
            dramatic_print("\n🌙 The sun sets over Babylon. The den is silent...")
            for _ in range(3):
                time.sleep(1)
                sys.stdout.write(". ")
                sys.stdout.flush()
            print("\n")
        
        elif your_decision_den.lower() == 'q':
            dramatic_print("🌅 The King retires to his chambers. The End.")
            break
        else:
            dramatic_print(f"🕊️  You look away, allowing {citizen.name} to slip into the shadows.")
            citizens.append(citizen) 
            continue

        # Checking the status
        your_decision_check = input("\n👀 Dawn has come. Check the lions' status? (y/n): ") 
        if your_decision_check.lower() == 'y':
            time.sleep(1)
            babylon_den.check_lions()

import kingdom

# --- 3. THE DEN ---
class AngelDen(kingdom.Den):
    def __init__(self, lions_list):
        super().__init__(lions_list)
        self.angel_present = False

    def throw_in(self, person):
        print(f"\n[!] {person.name} has been cast into the den for praying to {person.god_of_choice}.")
        
        if person.god_of_choice == "God of Israel":
            self.angel_present = True
        else:
            self.angel_present = False
            super().throw_in(person)

    def check_lions(self):          
        print("\n--- Lion Status Report ---")
        if self.angel_present:
             dramatic_print("A divine presence is felt in the den... A miracle happened!")
             for lion in self.lions:
                status = "Hungry/Peaceful (Miracle)" if lion.hunger_level > 0 else "Satiated"
                print(f"Lion {lion.name}: {status} (Hunger Level: {lion.hunger_level})")
        else:
            super().check_lions()