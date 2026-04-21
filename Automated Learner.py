import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

class AutomatedLearner:
    def __init__(self, model_type="Linear"):
        self.model = LinearRegression()
        self.imputer = SimpleImputer(strategy='mean')
        self.is_fitted = False
        print(f"--- {model_type} Pipeline Initialized ---")

    def __clean_data(self, df):
        """Internal helper to handle missing values."""
        print("🛠  Cleaning data...")
        # Fits the imputer to fill NaNs with the average of the column
        return self.imputer.fit_transform(df)

    def train_pipeline(self, X_raw, y):
        """The 'Meat' of the pipeline: Clean -> Fit."""
        X_clean = self.__clean_data(X_raw)
        
        print("🏋️  Training model...")
        self.model.fit(X_clean, y)
        self.is_fitted = True
        print("✅ Pipeline ready for deployment.")

    def get_prediction(self, new_data):
        """Ensures data is cleaned exactly like the training data before predicting."""
        if not self.is_fitted:
            raise Exception("Model must be trained before predicting!")
            
        # We must transform new data using the same imputer rules
        cleaned_input = self.imputer.transform(new_data)
        prediction = self.model.predict(cleaned_input)
        return prediction

# --- Execution ---
if __name__ == "__main__":
    # Simulated Raw Data (with a missing value in the second row)
    raw_features = pd.DataFrame({'Size': [500, 700, 800, 1000], 'Rooms': [1, None, 3, 4]})
    target_prices = [150, 200, 250, 300]

    # Initialize the object
    ai_pipe = AutomatedLearner()

    # One call to handle everything
    ai_pipe.train_pipeline(raw_features, target_prices)

    # Make a prediction on a new house [900 sq ft, 2 rooms]
    result = ai_pipe.get_prediction([[900, 2]])
    print(f"🔮 Predicted Value: ${result[0]:.2f}k")
