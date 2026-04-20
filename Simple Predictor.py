class SimplePredictor:
    def __init__(self, model_name, accuracy_threshold):
        # 'self' refers to the specific object being created
        self.name = model_name
        self.threshold = accuracy_threshold
        self.is_trained = False

    def train(self, data):
        print(f"🌀 Training the {self.name} model using {len(data)} rows...")
        self.is_trained = True
        print("✅ Training Complete.")

    def predict(self, input_val):
        if not self.is_trained:
            return "❌ Error: Model must be trained first!"
        return f"🔮 {self.name} predicts: {input_val * 1.5}"

# --- Using the Class ---
# We create two different "Instances" (Objects) of the same class
churn_model = SimplePredictor("Churn_v1", 0.85)
sales_model = SimplePredictor("Sales_Forecaster", 0.90)

churn_model.train([10, 20, 30])
print(churn_model.predict(100))
