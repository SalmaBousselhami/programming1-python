"""Classes for representing citizens of the kingdom."""

class Citizen:
    """Represent a citizen of the kingdom."""
    
    def __init__(self, name, age):
        """Initialize attributes to describe a citizen."""
        self.name = name
        self.age = age
    
    def get_description(self):
        """Return a formatted description of the citizen."""
        return f"{self.name}, age {self.age}"
    
    def pay_taxes(self):
        """Pay taxes to the kingdom."""
        print(f"{self.name} pays taxes to the kingdom.")