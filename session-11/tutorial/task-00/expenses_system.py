class ExpenseReport:
    """Tracks and manages expense reports for a traveler."""
     
    def __init__(self, person: str, destination: str, stated_total: float = 0.0, 
                 reason: str = "", items: list = None) -> None:
        self.person = person
        self.destination = destination
        self.stated_total = stated_total
        self.reason = reason
        self.items = items if items is not None else []

    def addItem(self, item: 'Item') -> None:
        """Add an item to the expense report."""
        self.items.append(item)

    def sumExpenses(self) -> float:
        """Calculate the total sum of all expenses."""
        expenses_total = 0.0

        for item in self.items:
            expenses_total += item.amount

        return expenses_total
    
    def is_suspicious(self) -> bool:
        """
        This is the Gestapo-Method!!!
        Check if the expense report is suspicious.
        Returns True if:
        - Stated and actual totals don't match (and wasn't resolved)
        - Reason contains suspicious persons (e.g., 'Dohnanyi')
        """
        # Check if there's a mismatch between stated and actual totals
        actual_total = self.sumExpenses()
        if abs(actual_total - self.stated_total) > 0.01:  # Small tolerance for rounding
            print(f"⚠️  Hint: Discrepancy between Actual total ${actual_total:.2f} vs Stated total ${self.stated_total:.2f}")
            return True
        
        # List of suspicious/ungraceful persons to watch for
        suspicious_persons = ['dohnanyi']
        
        # Check if any suspicious persons are mentioned in the reason
        for item in self.items:
            description_lower = item.description.lower()
            for person in suspicious_persons:
                if person in description_lower:
                    print(f"⚠️  Hint: Suspicious person '{person}' mentioned in item description: {item.description}")
                    return True

        return False
    
    def __str__(self) -> str:
        """
        Format and return the expense report as a formatted string.
        """
        output = f"\n{'='*60}\n"
        output += f"Traveler: {self.person}\n"
        output += f"Destination: {self.destination}\n"
        output += f"Trip Purpose: {self.reason}\n"
        output += f"Stated Total: ${self.stated_total:.2f}\n"
        output += f"Number of items: {len(self.items)}\n"
        output += f"\nExpense items:\n"
        
        for item in self.items:
            output += f"  - {item.category}: ${item.amount:.2f} ({item.description})\n"
        
        actual_total = self.sumExpenses()
        output += f"\nActual Total: ${actual_total:.2f}\n"
        
        return output

class Item:
    """Represents a single expense item."""
    
    def __init__(self, category: str, amount: float, description: str) -> None:
        self.category = category
        self.amount = amount if amount else 0.0
        self.description = description
    
    def __repr__(self) -> str:
        return f"Item({self.category}, {self.amount}, {self.description})"
    