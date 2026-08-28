# Dr. Bonhoeffer's Travel Expense Management System (Extended)

## Overview

This is an interactive expense management system that allows users to work with Dr. Dietrich Bonhoeffer's historical travel expense reports. Unlike the basic version, this extended version provides a full interactive menu system where users can:

- Load expense reports from text files
- View and edit expense details
- Delete individual expense items
- Modify stated totals
- Save reports to JSON format
- View, edit, and manage JSON files
- List all available reports

## Features

### 1. Load and Edit TXT Expense Reports
- Automatically discovers all `.txt` files in the `travel_expense_reports/` directory
- Select a report to edit
- View the full expense breakdown
- Delete items that are suspicious or incorrect
- Modify the stated total if needed
- Save edited reports to JSON format

### 2. View and Edit JSON Expense Reports
- View all saved JSON reports
- Edit individual JSON reports (change totals, delete items)
- Save changes back to the JSON file
- Delete JSON files with confirmation

### 3. List Available JSON Files
- See all JSON reports with a quick summary
- View traveler name, destination, total, and item count
- Easily identify which reports have been saved

## How to Use

### Running the Program
```bash
python main.py
```

### Main Menu Options

#### Option 1: Load and Edit TXT Expense Reports
1. Select from available reports
2. View the expense breakdown
3. Choose to:
   - Delete an item (useful for removing suspicious expenses)
   - Change the stated total (adjust the reported total)
   - View full details (comprehensive expense breakdown)
   - Save to JSON (export the edited report)

#### Option 2: View and Edit JSON Expense Reports
1. Select from available JSON files
2. Make edits as needed
3. Save changes or delete the file

#### Option 3: List Available JSON Files
- View all JSON reports with their key details
- Get a quick overview without opening files

#### Option 4: Exit
- Safely close the program

## File Structure

```
08_bonhoeffers_travel_expenses_extended/
├── main.py                          # Interactive menu system
├── expenses_system.py               # ExpenseReport and Item classes
├── preprocessing.py                 # File reading and parsing functions
├── README.md                        # This file
├── travel_expense_reports/          # Text files with original data
│   ├── trip_munich.txt
│   ├── trip_vatican.txt
│   ├── trip_stockholm.txt
│   └── trip_zurich.txt
└── json_reports/                    # Directory created when saving JSON files
    └── (saved reports will appear here)
```

## Learning Objectives

By working with this interactive system, students will learn:

1. **User Interaction**: How to build interactive menu-driven programs
2. **File I/O**: Reading from and writing to both text and JSON files
3. **Data Manipulation**: Modifying and validating expense data
4. **JSON Operations**: Serializing objects to JSON and deserializing back
5. **Error Handling**: Managing file errors and invalid input
6. **Functions and Modularity**: Breaking code into logical, reusable functions
7. **Data Structures**: Working with lists and dictionaries effectively

## Example Workflow

1. Start the program
2. Select "Load and Edit TXT Expense Reports"
3. Choose a report (e.g., Munich)
4. View the expenses and notice any issues (missing amounts, suspicious persons)
5. Delete suspicious items or fix the stated total
6. Save the corrected report to JSON
7. Exit back to main menu
8. Select "View and Edit JSON Expense Reports"
9. Open the Munich report you just saved
10. Make further edits if needed
11. Save changes and return to main menu

## Historical Context

Dr. Dietrich Bonhoeffer (1906-1945) was a German Lutheran theologian and anti-Nazi dissident. He traveled extensively for ecumenical work and resistance activities. His expense reports reflect the various trips he took during this crucial period in history.

### Sample Destinations:
- **Munich**: Ecumenical discussions with German church leaders
- **Vatican**: Vatican diplomatic mission and papal audience
- **Stockholm**: Ecumenical conference and resistance coordination
- **Zurich**: Swiss church consultation and ecumenical planning

## Technical Notes

- The system uses Python's `pathlib` for robust file path handling
- JSON files are formatted with indentation for human readability
- All amounts are stored and displayed in USD format
- The system validates input and provides helpful error messages
- Directory creation is automatic (json_reports folder created on first save)

## Potential Extensions

Students could extend this system by adding:
- Database storage (SQLite)
- Summary reports and statistics
- Expense categorization and filtering
- Receipt validation
- Multi-currency support
- Audit logging of all changes
