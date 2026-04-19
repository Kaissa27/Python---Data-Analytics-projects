import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

def predict_customer_churn():
    # 1. THE DATASET (X = Features, y = Target)
    # Features: [Monthly_Usage_Hours, Support_Tickets]
    # Target: 0 (Stayed), 1 (Churned/Left)
    X = np.array([
        [40, 0], [50, 1], [35, 0], [60, 1], # Happy customers (Stayed)
        [5, 4], [10, 5], [2, 3], [8, 4]      # Frustrated customers (Left)
    ])
    y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

    # 2. INITIALIZE & TRAIN
    # We use Logistic Regression for Binary Classification
    model = LogisticRegression()
    model.fit(X, y)

    # 3. PREDICTING FOR NEW CUSTOMERS
    # Customer A: High usage (45 hrs), 1 support ticket
    # Customer B: Low usage (12 hrs), 4 support tickets
    new_customers = np.array([[45, 1], [12, 4]])
    predictions = model.predict(new_customers)
    probabilities = model.predict_proba(new_customers) # The % chance

    print("--- 📉 Churn Prediction Report ---")
    for i, pred in enumerate(predictions):
        status = "CHURN ALERT (Likely to Leave)" if pred == 1 else "SAFE (Likely to Stay)"
        risk_pct = probabilities[i][1] * 100
        print(f"Customer {i+1}: {status} | Risk Level: {risk_pct:.1f}%")

    # 4. INSIGHT: Model Coefficients
    # Tells us which feature matters more
    print("-" * 45)
    print(f"Usage Influence: {model.coef_[0][0]:.2f}")
    print(f"Support Ticket Influence: {model.coef_[0][1]:.2f}")

if __name__ == "__main__":
    predict_customer_churn()
