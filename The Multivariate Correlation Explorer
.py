import pandas as pd
import seaborn as sns # Standard for visual correlations

def analyze_multivariate_relationships():
    # 1. GENERATE DATA
    # We're creating data for 100 different store locations
    data = {
        'Revenue': [10, 25, 12, 45, 30, 18, 50, 22, 14, 35] * 10,
        'Marketing_Spend': [2, 5, 2, 8, 4, 3, 9, 3, 2, 6] * 10,
        'Staff_Count': [3, 4, 2, 6, 5, 3, 7, 3, 2, 5] * 10,
        'Customer_Rating': [4.1, 4.5, 3.8, 4.8, 4.2, 3.9, 4.9, 4.0, 3.7, 4.6] * 10,
        'Temperature_Outside': [22, 25, 20, 28, 24, 21, 30, 23, 19, 26] * 10
    }
    
    df = pd.DataFrame(data)

    # 2. CALCULATE CORRELATION MATRIX
    # This uses the 'Pearson' method by default
    # Values range from -1 (Opposite) to 1 (Perfect Match)
    corr_matrix = df.corr()

    print("--- 📊 Correlation Matrix ---")
    print(corr_matrix.round(2))

    # 3. INTERPRETING THE DATA
    # Let's find what has the strongest relationship with Revenue
    rev_corr = corr_matrix['Revenue'].sort_values(ascending=False)
    
    print("\n--- Relationship with Revenue (Top Drivers) ---")
    print(rev_corr)

    # 4. INSIGHT LOGIC
    top_driver = rev_corr.index[1] # Index 0 is Revenue itself
    strength = rev_corr[1]
    
    print(f"\n[INSIGHT]: The strongest driver of Revenue is '{top_driver}' ({strength:.2f}).")
    if strength > 0.8:
        print("ACTION: Focus budget heavily on this variable.")

if __name__ == "__main__":
    analyze_multivariate_relationships()
