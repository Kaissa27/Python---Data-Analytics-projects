def monthly_sales_report():
    # Raw Data: (Date, Amount)
    # This represents individual sales happening throughout the quarter
    daily_sales = [
        ("2024-01-05", 150), ("2024-01-12", 200), ("2024-02-03", 50),
        ("2024-02-15", 300), ("2024-02-28", 100), ("2024-03-10", 450),
        ("2024-03-22", 200), ("2024-03-31", 150)
    ]

    # 1. The Aggregation Dictionary
    # Key = Month, Value = Total Sales
    monthly_totals = {}

    for date, amount in daily_sales:
        # Extract the month (e.g., "2024-01" from "2024-01-05")
        month = date[:7] 
        
        # Add the amount to that month's total
        if month not in monthly_totals:
            monthly_totals[month] = 0
        monthly_totals[month] += amount

    # 2. Performance Analysis
    print("--- Quarterly Sales Summary ---")
    print(f"{'Month':<10} | {'Total Sales':<12} | {'Status'}")
    print("-" * 35)

    # Sort months chronologically
    for month in sorted(monthly_totals.keys()):
        total = monthly_totals[month]
        
        # Add a simple 'Performance Tag'
        status = "🔥 High" if total > 400 else "Neutral"
        print(f"{month:<10} | ${total:<11} | {status}")

    # 3. Growth Calculation
    months = sorted(monthly_totals.keys())
    jan_sales = monthly_totals[months[0]]
    mar_sales = monthly_totals[months[-1]]
    growth = ((mar_sales - jan_sales) / jan_sales) * 100

    print("-" * 35)
    print(f"Total Growth (Jan to Mar): {growth:+.1f}%")

monthly_sales_report()