import math

def inventory_velocity_analysis():
    # Data: { Product_ID: {"stock": current_units, "sales_7_days": [daily_units_sold]} }
    inventory_data = {
        "SKU_101": {"stock": 150, "sales_7_days": [20, 25, 18, 22, 19, 21, 25]},
        "SKU_102": {"stock": 40,  "sales_7_days": [10, 12, 15, 11, 14, 13, 15]},
        "SKU_103": {"stock": 500, "sales_7_days": [2, 1, 3, 0, 1, 2, 1]},
        "SKU_104": {"stock": 12,  "sales_7_days": [5, 6, 4, 7, 5, 8, 6]}
    }

    print(f"{'Product ID':<10} | {'Stock':<6} | {'Daily Avg':<10} | {'Days Left':<10} | {'Status'}")
    print("-" * 65) 

    for sku, info in inventory_data.items():
        # 1. Calculate Velocity (Average units sold per day)
        daily_avg = sum(info["sales_7_days"]) / len(info["sales_7_days"])
        
        # 2. Calculate "Runway" (Stock / Daily Avg)
        # We use math.floor because you can't have a partial day of sales
        if daily_avg > 0:
            days_left = math.floor(info["stock"] / daily_avg)
        else:
            days_left = float('inf') # Infinite days if no sales

        # 3. Alert Logic (Priority Ranking)
        if days_left <= 3:
            status = "🚨 CRITICAL"
        elif days_left <= 7:
            status = "⚠️ REORDER"
        elif daily_avg < 1:
            status = "💤 STAGNANT"
        else:
            status = "✅ HEALTHY"

        print(f"{sku:<10} | {info['stock']:<6} | {daily_avg:>10.1f} | {days_left:>10} | {status}")

inventory_velocity_analysis()