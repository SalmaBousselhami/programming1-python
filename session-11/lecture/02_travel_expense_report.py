from pathlib import Path

report_path = Path(__file__).parent / 'travel_expense_reports' / 'trip_stockholm.txt'

print("Processing travel expense report...\n")

try:
    contents = report_path.read_text(encoding='utf-8')
    lines = contents.strip().split('\n')
    
    # Calculate total expenses
    total = 0
    
    for line in lines[1:]:  # Skip header
        parts = line.split(',')
        amount = float(parts[-1]) # Here is the bug!
        total += amount
    
    print(f"Report processed successfully!")
    print(f"Total expenses: ${total:.2f}")
    
except FileNotFoundError:
    print(f"Error: Report file not found at '{report_path}'")
except ValueError:
    print("Error: Invalid data format in the expense report.")
    # x = 5/0 # Here we case a new Exception
except:
    print("An unexpected error occurred during processing.")
finally:
    print("\n--- Processing complete ---")
    print("Report processing session ended.")

print("\nGoodbye!")