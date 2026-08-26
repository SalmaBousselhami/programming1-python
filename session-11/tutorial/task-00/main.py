from preprocessing import load_expense_reports, reconcile_report_totals, remove_suspicious_items

# Read the Expense reports
reports = load_expense_reports()

# Reconcile each report
for index, report in enumerate(reports):
    print(f"\n{'='*60}")
    print(f"Processing Report {index + 1}: {report.destination}")
    report = remove_suspicious_items(report)
    reports[index] = reconcile_report_totals(report)

# 🚨 The Gestapo Audit starts 🚨   
# Display information about each report
for report in reports:
    print(report)
    
    # Check if report is suspicious
    if report.is_suspicious():
        print(f"🚨 SUSPICIOUS: This report requires further review!")
    else:
        print(f"✅ This report appears to be in order.")

