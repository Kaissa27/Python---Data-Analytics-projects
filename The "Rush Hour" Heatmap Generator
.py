import pandas as pd
import numpy as np

def generate_hourly_heatmap():
    # 1. GENERATE SYNTHETIC DATA
    # 1000 random transactions over a week
    dr = pd.date_range(start='2026-04-01', end='2026-04-07', freq='H')
    
    # Simulate random sales volume (higher during 8-10 AM and 4-6 PM)
    data = []
    for dt in dr:
        hour = dt.hour
        # Logic: If morning/evening rush, boost sales
        if (8 <= hour <= 10) or (16 <= hour <= 18):
            sales = np.random.randint(20, 50)
        else:
            sales = np.random.randint(5, 15)
        data.append({'Timestamp': dt, 'Sales': sales})

    df = pd.DataFrame(data)

    # 2. TIME FEATURE EXTRACTION
    df['Day'] = df['Timestamp'].dt.day_name()
    df['Hour'] = df['Timestamp'].dt.hour

    # 3. THE PIVOT TABLE
    # Rows = Hours, Columns = Days, Values = Sum of Sales
    # This turns a long list into a 24x7 matrix
    heatmap_data = df.pivot_table(
        index='Hour', 
        columns='Day', 
        values='Sales', 
        agg_agg='sum'
    )

    # Reorder columns to follow a standard week
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_data = heatmap_data.reindex(columns=days_order)

    print("--- Hourly Sales Heatmap (Sample: Morning Rush) ---")
    # Displaying hours 7 AM to 11 AM across the week
    print(heatmap_data.iloc[7:12])

    # 4. INSIGHT EXTRACTION
    # Finding the absolute peak hour across the entire week
    max_val = heatmap_data.max().max()
    peak_hour = (heatmap_data == max_val).stack().idxmax()
    
    print("-" * 50)
    print(f" TOTAL PEAK: {peak_hour[0]}:00 on {peak_hour[1]} with {max_val} sales.")

if __name__ == "__main__":
    generate_hourly_heatmap()
