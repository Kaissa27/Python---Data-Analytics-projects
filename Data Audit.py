import pandas as pd
import numpy as np

def data_cleansing_suite():
    # Raw Data with missing values (None/NaN) and duplicates
    data = {
        'Customer': ['Alice', 'Bob', 'Charlie', 'Alice', 'Eve', 'Frank'],
        'Spent': [150.0, 200.0, np.nan, 150.0, 300.0, np.nan],
        'Region': ['North', 'South', 'North', 'North', 'West', None]
    }

    df = pd.DataFrame(data)

    print("--- 1. Initial Data Audit ---")
    # .isnull().sum() is the first thing every analyst runs to find "holes"
    print(df.isnull().sum())
    
    # 2. Handling Duplicates
    # Alice is in here twice with the same data. Let's fix that.
    df = df.drop_duplicates()

    # 3. Handling Missing Numbers (Imputation)
    # Instead of deleting Charlie and Frank, we fill their 'Spent' with the average
    avg_spend = df['Spent'].mean()
    df['Spent'] = df['Spent'].fillna(avg_spend)

    # 4. Handling Missing Categories
    # For missing Regions, we use a placeholder "Unknown"
    df['Region'] = df['Region'].fillna('Unknown')

    print("\n--- 2. Cleaned Dataset ---")
    print(df)

    print(f"\nAudit Note: Replaced missing spend values with the average of ${avg_spend:.2f}")

if __name__ == "__main__":
    data_cleansing_suite()
