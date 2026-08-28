import json
from pathlib import Path
from expenses_system import ExpenseReport, Item
from preprocessing import load_expense_reports, reconcile_report_totals, remove_suspicious_items


def print_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("Dr. Bonhoeffer's Travel Expense Management System")
    print("="*60)
    print("\n1. Load and Edit TXT Expense Reports")
    print("2. View and Edit JSON Expense Reports")
    print("3. List Available JSON Files")
    print("4. Exit")
    print("\n" + "-"*60)


def load_txt_menu():
    """Menu for loading and editing TXT files."""
    while True:
        print("\n" + "="*60)
        print("Load TXT Expense Reports")
        print("="*60)
        
        # Load all available reports
        reports = load_expense_reports()
        
        if not reports:
            print("No expense reports found.")
            return
        
        print(f"\nFound {len(reports)} expense reports:\n")
        for idx, report in enumerate(reports, 1):
            print(f"{idx}. {report.destination} - {report.person}")
        
        print(f"{len(reports) + 1}. Back to Main Menu")
        
        choice = input("\nSelect a report to edit (or go back): ").strip()
        
        try:
            choice_num = int(choice)
            if choice_num == len(reports) + 1:
                return
            if 1 <= choice_num <= len(reports):
                edit_txt_report(reports[choice_num - 1])
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def edit_txt_report(report: ExpenseReport):
    """Menu for editing a single TXT report."""
    while True:
        print(report)
        print("\nEdit Options:")
        print("1. Delete an item")
        print("2. Change stated total")
        print("3. View full details")
        print("4. Save to JSON")
        print("5. Back to TXT Menu")
        print("-"*60)
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            delete_item(report)
        elif choice == "2":
            change_stated_total(report)
        elif choice == "3":
            view_report_details(report)
        elif choice == "4":
            save_report_to_json(report)
        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")


def delete_item(report: ExpenseReport):
    """Delete an item from the expense report."""
    if not report.items:
        print("No items to delete.")
        return
    
    print("\nItems in this report:")
    for idx, item in enumerate(report.items, 1):
        print(f"{idx}. {item.category}: ${item.amount:.2f} ({item.description})")
    
    try:
        choice = int(input("\nSelect item number to delete (0 to cancel): ").strip())
        if choice == 0:
            return
        if 1 <= choice <= len(report.items):
            deleted = report.items.pop(choice - 1)
            print(f"✅ Deleted: {deleted.category} - ${deleted.amount:.2f}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")


def change_stated_total(report: ExpenseReport):
    """Change the stated total of the report."""
    print(f"Current stated total: ${report.stated_total:.2f}")
    print(f"Actual total (sum of items): ${report.sumExpenses():.2f}")
    
    try:
        new_total = float(input("Enter new stated total: $").strip())
        if new_total >= 0:
            report.stated_total = new_total
            print(f"✅ Stated total updated to: ${new_total:.2f}")
        else:
            print("Total must be non-negative.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def view_report_details(report: ExpenseReport):
    """Display detailed information about the report."""
    print("\n" + "="*60)
    print("EXPENSE REPORT DETAILS")
    print("="*60)
    print(f"Traveler: {report.person}")
    print(f"Destination: {report.destination}")
    print(f"Trip Purpose: {report.reason}")
    print(f"Stated Total: ${report.stated_total:.2f}")
    print(f"Actual Total (sum): ${report.sumExpenses():.2f}")
    print(f"Discrepancy: ${abs(report.stated_total - report.sumExpenses()):.2f}")
    
    print(f"\nExpense Items ({len(report.items)} total):")
    for idx, item in enumerate(report.items, 1):
        print(f"  {idx}. {item.category}: ${item.amount:.2f} ({item.description})")
    print("="*60)


def save_report_to_json(report: ExpenseReport):
    """Save the edited report to a JSON file."""
    # Create json_reports directory if it doesn't exist
    json_dir = Path(__file__).parent / 'json_reports'
    json_dir.mkdir(exist_ok=True)
    
    # Generate filename from destination
    filename = f"{report.destination.lower()}_report.json"
    file_path = json_dir / filename
    
    # Convert report to dictionary
    report_dict = {
        "person": report.person,
        "destination": report.destination,
        "reason": report.reason,
        "stated_total": report.stated_total,
        "items": [
            {
                "category": item.category,
                "amount": item.amount,
                "description": item.description
            }
            for item in report.items
        ]
    }
    
    # Save to JSON
    try:
        with open(file_path, 'w') as f:
            json.dump(report_dict, f, indent=2)
        print(f"✅ Report saved to: {filename}")
    except IOError as e:
        print(f"❌ Error saving file: {e}")


def json_menu():
    """Menu for viewing and editing JSON files."""
    while True:
        print("\n" + "="*60)
        print("JSON Expense Reports")
        print("="*60)
        
        json_files = list_json_files()
        
        if not json_files:
            print("No JSON reports found.")
            choice = input("\nPress Enter to go back to Main Menu...")
            return
        
        print("\nOptions:")
        for idx, filename in enumerate(json_files, 1):
            print(f"{idx}. {filename}")
        print(f"{len(json_files) + 1}. Back to Main Menu")
        print("-"*60)
        
        choice = input("Select a report to view/edit: ").strip()
        
        try:
            choice_num = int(choice)
            if choice_num == len(json_files) + 1:
                return
            if 1 <= choice_num <= len(json_files):
                edit_json_report(json_files[choice_num - 1])
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")


def list_json_files():
    """List all available JSON report files."""
    json_dir = Path(__file__).parent / 'json_reports'
    if not json_dir.exists():
        return []
    
    json_files = sorted([f.name for f in json_dir.glob('*.json')])
    return json_files


def edit_json_report(filename: str):
    """Menu for editing a single JSON report."""
    json_dir = Path(__file__).parent / 'json_reports'
    file_path = json_dir / filename
    
    try:
        with open(file_path, 'r') as f:
            report_data = json.load(f)
        
        # Convert to ExpenseReport object
        report = ExpenseReport(
            person=report_data['person'],
            destination=report_data['destination'],
            stated_total=report_data['stated_total'],
            reason=report_data['reason'],
            items=[
                Item(item['category'], item['amount'], item['description'])
                for item in report_data['items']
            ]
        )
        
        while True:
            print(report)
            print("\nEdit Options:")
            print("1. Delete an item")
            print("2. Change stated total")
            print("3. View full details")
            print("4. Save changes")
            print("5. Delete this file")
            print("6. Back to JSON Menu")
            print("-"*60)
            
            choice = input("Select an option: ").strip()
            
            if choice == "1":
                delete_item(report)
            elif choice == "2":
                change_stated_total(report)
            elif choice == "3":
                view_report_details(report)
            elif choice == "4":
                save_json_report(file_path, report)
            elif choice == "5":
                if confirm_delete():
                    file_path.unlink()
                    print(f"✅ File deleted: {filename}")
                    return
            elif choice == "6":
                return
            else:
                print("Invalid choice.")
    
    except json.JSONDecodeError:
        print("❌ Error reading JSON file. File may be corrupted.")
    except IOError as e:
        print(f"❌ Error reading file: {e}")


def save_json_report(file_path: Path, report: ExpenseReport):
    """Save the edited report back to JSON file."""
    report_dict = {
        "person": report.person,
        "destination": report.destination,
        "reason": report.reason,
        "stated_total": report.stated_total,
        "items": [
            {
                "category": item.category,
                "amount": item.amount,
                "description": item.description
            }
            for item in report.items
        ]
    }
    
    try:
        with open(file_path, 'w') as f:
            json.dump(report_dict, f, indent=2)
        print(f"✅ Changes saved to: {file_path.name}")
    except IOError as e:
        print(f"❌ Error saving file: {e}")


def confirm_delete():
    """Ask for confirmation before deleting."""
    response = input("Are you sure? This cannot be undone. (yes/no): ").strip().lower()
    return response == 'yes'


def list_json_files_menu():
    """Display all JSON files with their details."""
    print("\n" + "="*60)
    print("Available JSON Expense Reports")
    print("="*60)
    
    json_files = list_json_files()
    
    if not json_files:
        print("No JSON reports found.")
    else:
        json_dir = Path(__file__).parent / 'json_reports'
        for filename in json_files:
            file_path = json_dir / filename
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                print(f"\n📄 {filename}")
                print(f"   Traveler: {data['person']}")
                print(f"   Destination: {data['destination']}")
                print(f"   Stated Total: ${data['stated_total']:.2f}")
                print(f"   Items: {len(data['items'])}")
            except (json.JSONDecodeError, IOError):
                print(f"\n❌ {filename} (Error reading file)")
    
    print("\n" + "="*60)
    input("Press Enter to continue...")


def main():
    """Main program loop."""
    while True:
        print_menu()
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            load_txt_menu()
        elif choice == "2":
            json_menu()
        elif choice == "3":
            list_json_files_menu()
        elif choice == "4":
            print("\nGoodbye! Bonhoeffer's records are secured.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

