import csv 

def export_analytics_report():
    # 1. The Processed Data (from our previous analysis steps)
    # This is a list of dictionaries, which is the standard "Data Row" format
    report_data = [
        {"Month": "Jan", "Revenue": 12000, "Expenses": 8000, "Profit": 4000},
        {"Month": "Feb", "Revenue": 15000, "Expenses": 8500, "Profit": 6500},
        {"Month": "Mar", "Revenue": 11000, "Expenses": 9000, "Profit": 2000},
        {"Month": "Apr", "Revenue": 18000, "Expenses": 9500, "Profit": 8500}
    ]

    # 2. Define the Filename
    filename = "monthly_financial_summary.csv"

    # 3. The Writing Process
    # 'w' means write mode, newline='' prevents extra blank rows in Excel
    try:
        with open(filename, mode='w', newline='') as file:
            # Create a header based on the keys of the first dictionary
            fieldnames = report_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the top row (Header)
            writer.writeheader()
            
            # Write all the data rows
            writer.writerows(report_data)

        print(f"--- Export Successful ---")
        print(f"File '{filename}' has been created in your project folder.")
        print("You can now open this file in Excel or Google Sheets!")

    except IOError:
        print("Error: Could not write to file. Is it open in another program?")

if __name__ == "__main__":
    export_analytics_report()