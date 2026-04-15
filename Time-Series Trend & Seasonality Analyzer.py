import pandas as pd
import numpy as np

def analyze_time_trends():
    # 1. GENERATE SYNTHETIC DATA
    # Creating 30 days of data with a "weekend boost" and some random noise
    dates = pd.date_range(start='2026-03-01', periods=30)
    base_sales = 500
    
    # Logic: Add $200 if it's a Saturday(5) or Sunday(6), plus random noise
    sales = [
        base_sales + (200 if d.weekday() >= 5 else 0) + np.random.randint(-50, 50) 
        for d in dates
    ]

    df = pd.DataFrame({'Date': dates, 'Sales': sales})

    # 2. FEATURE ENGINEERING: Time Parts
    # Extracting the day name to see "Day of Week" performance
    df['Day_Name'] = df['Date'].dt.day_name()

    # 3. ROLLING METRICS (Smoothing the noise)
    # The 'window=7' calculates the average of the current day + the 6 previous days
    df['7_Day_Moving_Avg'] = df['Sales'].rolling(window=7).mean()

    # 4. AGGREGATION: Is there a "Weekend Effect"?
    # We create a boolean column for Weekend vs Weekday
    df['Is_Weekend'] = df['Date'].dt.weekday >= 5
    weekend_comparison = df.groupby('Is_Weekend')['Sales'].mean()

    print("--- Time-Series Summary ---")
    print(df.tail(10)) # Look at the last 10 days to see the Moving Avg kick in

    print("\n--- Average Revenue: Weekday vs Weekend ---")
    print(f"Weekdays: ${weekend_comparison[False]:.2f}")
    print(f"Weekends: ${weekend_comparison[True]:.2f}")

    # 5. FINDING THE PEAK
    peak_day = df.loc[df['Sales'].idxmax()]
    print(f"\n🚀 Peak Performance: {peak_day['Date'].date()} ({peak_day['Day_Name']}) with ${peak_day['Sales']}")

if __name__ == "__main__":
    analyze_time_trends()
