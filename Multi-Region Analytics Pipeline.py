import csv
import math

def run_analytics_capstone():
    # 1. RAW DATA (Simulating an incoming data stream)
    # Format: [Date, Region, Product, Units, Price_Per_Unit]
    raw_data = [
        ["2025-01-01", "North", "Widget A", "50", "15.00"],
        ["2025-01-02", "South", "Widget B", "20", "25.50"],
        ["2025-01-03", "North", "Widget A", "None", "15.00"],  # Null Error
        ["2025-01-05", "West ", "Widget C", "100", "10.00"],
        ["2025-01-06", "North", "Widget B", "-5", "25.50"],   # Integrity Error
        ["2025-01-10", "South", "Widget A", "30", "15.00"],
        ["2025-01-12", "west", "Widget C", "80", "10.00"]     # Case Sensitivity Error
    ]

    processed_records = []
    error_log = []
    
    print("🚀 Starting Data Pipeline...")

    # 2. VALIDATION & CLEANING PHASE
    for row in raw_data:
        try:
            date, region, product, units, price = row
            
            # Standardize strings
            region = region.strip().title()
            
            # Handle missing or invalid numbers
            if units == "None" or int(units) <= 0:
                error_log.append(f"Skipped {product} in {region}: Invalid Units ({units})")
                continue
                
            # Convert types and calculate revenue
            u_count = int(units)
            p_val = float(price)
            revenue = u_count * p_val
            
            processed_records.append({
                "Date": date,
                "Region": region,
                "Revenue": revenue
            })
        except Exception as e:
            error_log.append(f"Critical error on row {row}: {e}")

    # 3. AGGREGATION PHASE (Grouping by Region)
    region_performance = {}
    for rec in processed_records:
        reg = rec["Region"]
        rev = rec["Revenue"]
        region_performance[reg] = region_performance.get(reg, 0) + rev

    # 4. INSIGHT GENERATION
    print("\n--- Region Performance Summary ---")
    total_revenue = sum(region_performance.values())
    
    final_report = []
    for reg, rev in region_performance.items():
        market_share = (rev / total_revenue) * 100
        print(f"{reg:<10} | ${rev:<10,.2f} | Share: {market_share:.1f}%")
        
        final_report.append({
            "Region": reg,
            "Total_Revenue": round(rev, 2),
            "Market_Share_Pct": round(market_share, 2)
        })

    # 5. EXPORT PHASE
    with open("final_sales_report.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Region", "Total_Revenue", "Market_Share_Pct"])
        writer.writeheader()
        writer.writerows(final_report)

    # 6. ERROR REPORTING
    if error_log:
        print("\n[!] Pipeline Alerts:")
        for err in error_log:
            print(f" - {err}")

    print(f"\n✅ Pipeline Complete. Report saved to 'final_sales_report.csv'")

if __name__ == "__main__":
    run_analytics_capstone()