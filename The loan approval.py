from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

def run_loan_decision_tree():
    # 1. THE DATASET
    # Features: [Credit_Score, Income_in_k]
    # Target: 0 (Deny), 1 (Approve)
    data = {
        'Credit_Score': [750, 450, 700, 500, 800, 600, 650, 550],
        'Income': [100, 30, 80, 40, 120, 55, 70, 45],
        'Approved': [1, 0, 1, 0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    X = df[['Credit_Score', 'Income']]
    y = df['Approved']

    # 2. INITIALIZE & TRAIN
    # We set max_depth to keep the tree simple and readable
    clf = DecisionTreeClassifier(max_depth=3)
    clf.fit(X, y)

    # 3. "PEEK" INSIDE THE BRAIN (The Logic)
    tree_rules = export_text(clf, feature_names=['Credit_Score', 'Income'])
    print("--- 🌳 Decision Tree Logic ---")
    print(tree_rules)

    # 4. PREDICT FOR A NEW APPLICANT
    # Applicant: 620 Credit Score, 65k Income
    applicant = [[620, 65]]
    prediction = clf.predict(applicant)
    
    result = "APPROVED" if prediction[0] == 1 else "DENIED"
    print("-" * 30)
    print(f"New Applicant Result: {result}")

if __name__ == "__main__":
    run_loan_decision_tree()
