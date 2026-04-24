import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def analyze_market_basket():
    # 1. THE DATA (Transactions)
    # Each row is a transaction, each column is an item
    data = {
        'Milk': [1, 1, 0, 1, 0],
        'Bread': [1, 1, 1, 0, 0],
        'Eggs': [0, 1, 0, 1, 0],
        'Butter': [0, 0, 1, 0, 1],
        'Coffee': [1, 1, 0, 1, 1]
    }
    df = pd.DataFrame(data)

    # 2. FIND FREQUENT ITEMSETS
    # We only care about items that appear in at least 30% of transactions
    frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

    # 3. GENERATE THE RULES
    # We look for rules with a 'Lift' greater than 1.0
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

    # 4. CLEAN UP THE OUTPUT
    # 'antecedents' is what they have, 'consequents' is what we predict
    result = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
    
    print("--- 🛒 Market Basket Insights ---")
    # Sorting by Lift to find the strongest relationships
    print(result.sort_values(by='lift', ascending=False).head(5))

if __name__ == "__main__":
    analyze_market_basket()
