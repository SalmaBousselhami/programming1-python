from expenses_system import ExpenseReport, Item
from pathlib import Path

def load_expense_reports():
    """Load all travel expense reports from files and reconcile them."""
    
    reports = []
    
    """
    FILE READING SECTION 1: LOCATE THE DATA DIRECTORY
    - Use the script's directory as the base (Path(__file__).parent)
    - Construct path to the travel_expense_reports subdirectory
    - This makes the script location-independent
    """
    script_dir = Path(__file__).parent
    report_dir = script_dir / 'travel_expense_reports'
    
    """
    FILE READING SECTION 2: VALIDATE DIRECTORY AND FILES EXIST
    - Check if the report directory exists
    - List all .txt files in the directory
    - Warn user if directory or files are missing
    """
    if not report_dir.exists():
        print(f"Error: Directory not found: {report_dir}")
        return reports
    
    txt_files = list(report_dir.glob('*.txt'))
    if not txt_files:
        print(f"Warning: No .txt files found in {report_dir}")
        return reports
    
    """
    FILE READING SECTION 3: PROCESS EACH EXPENSE FILE
    - Loop through each .txt file in sorted order
    - Extract destination from filename (trip_xxx.txt → Xxx)
    """
    for file_path in sorted(txt_files):
        # LOGIC: Extract destination from filename
        # Example: trip_munich.txt → munich → Munich
        filename = file_path.stem  # Remove .txt extension
        destination = filename.replace('trip_', '').title()  # Remove 'trip_' and capitalize
        
        """
        FILE READING SECTION 4: PARSE FILE CONTENTS
        - Initialize containers (variables) for parsed data
        - Read the entire file as text
        - Split into lines for line-by-line processing
        """
        items = []
        stated_total = 0.0
        reason = ""
        
        try:
            contents = file_path.read_text()
            lines = contents.strip().split('\n')
            
            """
            FILE READING SECTION 5: PROCESS EACH LINE
            - Strip whitespace from each line
            - Skip empty lines
            - Parse CSV format: category,amount,description
            """
            for line in lines:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                # LOGIC: Split CSV line into parts
                parts = line.split(',')
                
                if len(parts) >= 2:
                    category = parts[0].strip()
                    
                    """
                    FILE READING SECTION 6: HANDLE TOTAL LINE
                    - Detect if this is the special TOTAL line (first data row)
                    - Extract stated total amount
                    - Extract trip reason/purpose
                    - Skip adding this to items (it's metadata, not an expense)
                    """
                    if category.upper() == 'TOTAL':
                        try:
                            amount_str = parts[1].strip()
                            stated_total = float(amount_str) if amount_str else 0.0
                            reason = parts[2].strip() if len(parts) > 2 else ""
                        except (ValueError, IndexError):
                            print(f"Warning: Malformed TOTAL line in {file_path}: {line}")
                        continue
                    
                    """
                    FILE READING SECTION 7: PARSE REGULAR EXPENSE ITEMS
                    - Extract category (type of expense)
                    - Extract amount (handle missing values as 0.0)
                    - Extract description
                    - Create Item object and add to list
                    """
                    try:
                        amount_str = parts[1].strip()
                        amount = float(amount_str) if amount_str else 0.0
                        description = parts[2].strip() if len(parts) > 2 else ""
                        
                        item = Item(category, amount, description)
                        items.append(item)
                    except (ValueError, IndexError):
                        # Skip malformed lines
                        print(f"Warning: Skipping malformed line in {file_path}: {line}")
                        continue
        
        except FileNotFoundError:
            print(f"Warning: File {file_path} not found")
            continue
        
        """
        FILE READING SECTION 8: CREATE EXPENSE REPORT OBJECT
        - Instantiate ExpenseReport with all parsed data
        - Include person (always Dr. Dietrich Bonhoeffer)
        - Include destination (extracted from filename)
        - Include stated total and reason (from TOTAL line)
        - Include all parsed items
        """
        report = ExpenseReport(
            person="Dr. Dietrich Bonhoeffer",
            destination=destination,
            stated_total=stated_total,
            reason=reason,
            items=items
        )
        
        reports.append(report)
    
    return reports


def reconcile_report_totals(report: ExpenseReport) -> None:
    """
    Reconcile discrepancies between stated total and actual sum of expense items.
    """
    print(f"Reconciling report for {report.destination}...")

    """
    LOGIC SECTION 1: CHECK IF TOTALS MATCH
    - Calculate the actual sum of all items in the report
    - Compare with the stated total from the file header
    - If they match (within small tolerance), no action needed
    """
    actual_total = report.sumExpenses()
    
    # LOGIC: Only proceed if there's a meaningful discrepancy
    if abs(actual_total - report.stated_total) < 0.01:
        print("No discrepancy found; no reconciliation needed.")
        return report
    
    """
    LOGIC SECTION 2: IDENTIFY CORRUPTED DATA
    - Look for items where the amount is missing (0.0)
    - These represent corrupted or incomplete expense entries
    - Build a list of items that need fixing
    """
    items_with_missing_amounts = [item for item in report.items if item.amount == 0.0]
    
    """
    LOGIC SECTION 3: FALLBACK - ADJUST STATED TOTAL
    - If no corrupted items exist, the stated total must be wrong
    - Update the stated total to match the actual calculated sum
    - This preserves the data integrity of individual items
    """

    if not items_with_missing_amounts:
        print(f"No corrupted items found; adjusting stated total instead from ${report.stated_total:.2f} to ${actual_total:.2f}.")
        report.stated_total = actual_total 
        return report
    
    """
    LOGIC SECTION 4: ATTEMPT TO FIX CORRUPTED DATA
    - If corrupted items exist, calculate the difference between stated and actual
    - Distribute this difference among the corrupted items
    - Handle different cases: single missing item, multiple missing items
    """

    difference = report.stated_total - actual_total

    # Difference is negative or zero (adjust stated total)
    if difference < 0:
        print(f"Negative difference detected; adjusting stated total instead from ${report.stated_total:.2f} to ${actual_total:.2f}.")
        report.stated_total = actual_total
        return report
    
    # Distribute difference among corrupted items
    print(f"Distributing missing amount of ${difference:.2f} among {len(items_with_missing_amounts)} corrupted items.")
    for item in items_with_missing_amounts:
        item.amount += difference / len(items_with_missing_amounts)
        for index, value in enumerate(report.items):
            if value.description == item.description and value.category == item.category:
                print(f" - Updated item: {item.category}, new amount: ${item.amount:.2f}")
                report.items[index] = item

    return report


def remove_suspicious_items(report: ExpenseReport) -> None:
    """
    Remove items that mention suspicious persons from the expense report.
    """
    print(f"Removing suspicious items from report for {report.destination}...")
    
    # List of suspicious/ungraceful persons to watch for
    suspicious_persons = ['dohnanyi']
    
    # Filter out items that mention suspicious persons
    filtered_items = []
    for item in report.items:
        description_lower = item.description.lower()
        if any(person in description_lower for person in suspicious_persons):
            print(f" - Removing suspicious item: {item.category}, amount: ${item.amount:.2f}, description: {item.description}")
        else:
            filtered_items.append(item)
    
    report.items = filtered_items
    return report