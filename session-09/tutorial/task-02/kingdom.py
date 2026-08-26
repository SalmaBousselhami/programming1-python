# --- 1. THE PEOPLE ---
# First the Citizen class
class Citizen:
    def __init__(self, name, god_of_choice):
        self.name = name
        self.god_of_choice = god_of_choice

    def pray(self):
        # TODO: Implement the pray method (printing a message)
        pass

# Next the Minister class

class Minister():
    # TODO: Define a Minister class that inherits from Citizen
    # TODO: - Implement a suggest_law method that prints the suggested law
    
    pass


# --- 2. THE LIONS ---
class Lion:
    def __init__(self, name):
        self.name = name
        self.hunger_level = 10  # 10 is starving
    
    def eat(self, person):
        # TODO: Implement the eat method (printing a message and reducing hunger level to 0)
        
        pass

# --- 3. THE DEN ---
class Den:
    def __init__(self, lions_list):
        self.lions = lions_list

    def throw_in(self, person):
        # TODO: Implement the throw_in method 
        # TODO:   - printing messages
        # TODO:   - making lions eat the person if they are hungry, one person feeds one lion
        
        pass

    def check_lions(self): 
        # TODO: Implement the check_lions method
        # TODO:  - printing the status of each lion 
        
        pass