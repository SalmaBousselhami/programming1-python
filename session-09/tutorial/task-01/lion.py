class Lion:
    """A model of a lion in the den."""
    
    def __init__(self, name, age, strength):
        self.name = name
        self.age = age
        self.strength = strength
        self.hunger_level = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.name} the Lion - Age {self.age}, Strength {self.strength}"
        return long_name.title()
    
    def check_hunger(self):
        print(f"This lion's hunger level is {self.hunger_level}.")
    
    def set_hunger(self, level):
        if level <= 10:
            self.hunger_level = level
        else:
            print("Hunger level cannot exceed 10!")
    
    def feed_lion(self, meals):
        """Reduce hunger by the given number of meals (minimum 0)."""
        self.hunger_level = max(0, self.hunger_level - meals)