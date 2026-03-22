def calculate_marketing_roi(): 
    # Dataset 1: Monthly Ad Spend (Source: Marketing Dept)
    # Format: { Month: USD_Spent }
    ad_spend = {
        "Jan": 2500, "Feb": 3200, "Mar": 2800, 
        "Apr": 4100, "May": 3500, "Jun": 5000
    }

    # Dataset 2: Monthly Revenue (Source: Sales Dept)
    # Format: { Month: USD_Earned }
    sales_revenue = {
        "Jan": 8500, "Feb": 9100, "Mar": 12000, 
        "Apr": 11500, "May": 14200, "Jun": 19500
    }

    print(f"{'Month':<10} | {'Spend':<10} | {'Revenue':<10} | {'ROI %':<10}")
    print("-" * 50)

    performance_metrics = []

    # 1. Data Merging (The "Join" Operation)
    for month in ad_spend:
        spend = ad_spend[month]
        revenue = sales_revenue.get(month, 0) # Safety check if month is missing

        # 2. Calculating ROI: ((Revenue - Cost) / Cost) * 100
        profit = revenue - spend
        roi_percent = (profit / spend) * 100
        
        performance_metrics.append({
            "month": month,
            "roi": roi_percent,
            "efficiency": "High" if roi_percent > 300 else "Standard"
        })

        print(f"{month:<10} | ${spend:<9,} | ${revenue:<9,} | {roi_percent:>8.1f}%")

    # 3. Aggregated Insights
    avg_roi = sum(m['roi'] for m in performance_metrics) / len(performance_metrics)
    best_month = max(performance_metrics, key=lambda x: x['roi'])

    print("-" * 50)
    print(f"Average ROI for H1: {avg_roi:.1f}%")
    print(f"Top Performing Month: {best_month['month']} ({best_month['roi']:.1f}%)")

if __name__ == "__main__":
    calculate_marketing_roi()