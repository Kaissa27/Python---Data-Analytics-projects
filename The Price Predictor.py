from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Data: Square Footage (X) and House Price (y)
# Reshaping is required because Scikit-learn expects a 2D array for X
X = np.array([600, 800, 1000, 1200, 1500, 1800, 2000]).reshape(-1, 1)
y = np.array([200, 250, 280, 310, 380, 420, 480]) # Prices in thousands

# 2. Initialize and Train the Model
model = LinearRegression()
model.fit(X, y)

# 3. Predict the price for a 1700 sq ft house
new_house = np.array([[1700]])
prediction = model.predict(new_house)

print(f"Predicted Price for 1700 sq ft: ${prediction[0]:.2f}k")
print(f"Model Accuracy (R² Score): {model.score(X, y):.4f}")
