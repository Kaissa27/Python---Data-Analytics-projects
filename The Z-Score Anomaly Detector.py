import pandas as pd
import numpy as np

def detect_anomalies():
    # 1. GENERATE DATA
    # Most logins take 2-4 seconds. One takes 45 seconds (an outlier).
    data = {
        'User': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Login_Time': [2.1, 3.5, 2.8, 45.0, 3.1, 2.9, 3.3, 2.7, 3.8, 2.4]
    }
    df = pd.DataFrame(data)

    # 2. CALCULATE STATISTICS
    mean = df['Login_Time'].mean()
    std_dev = df['Login_Time'].std()

    # 3. CALCULATE THE Z-SCORE
    # The Z-Score tells us: "How many standard deviations is this value from the mean?"
    # Formula: (Value - Mean) / Standard Deviation
    df['Z_Score'] = (df['Login_Time'] - mean) / std_dev

    # 4. FLAG ANOMALIES
    # Threshold: Anything > 2.0 or < -2.0 is considered highly unusual
    threshold = 2.0
    df['Is_Anomaly'] = df['Z_Score'].abs() > threshold

    print("--- Security Audit: Login Latency ---")
    print(df)

    # 5. SUMMARY
    anomalies = df[df['Is_Anomaly']]
    if not anomalies.empty:
        print("\n[🚨 ALERT] Statistical Anomalies Detected:")
        for _, row in anomalies.iterrows():
            print(f" -> User {row['User']} flagged! Time: {row['Login_Time']}s (Z-Score: {row['Z_Score']:.2f})")
    else:
        print("\n✅ No anomalies detected.")

if __name__ == "__main__":
    detect_anomalies()
