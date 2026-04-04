def analyze_growth():
    # Dataset 1: Monthly Sales from 2024
    sales_2024 = [12000, 15000, 11000, 18000, 20000, 22000]
    
    # Dataset 2: Monthly Sales from 2025
    sales_2025 = [13500, 14200, 12500, 21000, 19000, 26000]
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

    print(f"{'Month':<10} | {'2024':<10} | {'2025':<10} | {'Change %'}")
    print("-" * 45)

    total_growth = 0

    # 1. Using zip() to iterate through both years simultaneously
    for month, old, new in zip(months, sales_2024, sales_2025):
        
        # 2. Calculating Percentage Variance
        # Formula: ((New - Old) / Old) * 100
        variance = ((new - old) / old) * 100
        total_growth += variance

        # 3. Dynamic Formatting (Coloring the "story" with symbols)
        indicator = "▲" if variance > 0 else "▼"
        
        print(f"{month:<10} | ${old:<9,} | ${new:<9,} | {indicator} {variance:>6.1f}%")

    # 4. Summary Insight
    avg_variance = total_growth / len(months)
    print("-" * 45)
    print(f"H1 Average Growth Rate: {avg_variance:+.2f}%")

    if avg_variance > 5:
        print("RESULT: Business is expanding significantly.")
    else:
        print("RESULT: Growth is stable/stagnant.")

analyze_growth()