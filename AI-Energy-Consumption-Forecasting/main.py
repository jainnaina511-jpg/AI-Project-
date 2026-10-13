import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Sample energy consumption data
data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Energy_Consumption": [120, 135, 128, 145, 160, 155, 170]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Day"]]
y = df["Energy_Consumption"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict energy consumption for Day 8
prediction = model.predict([[8]])

print(f"Predicted Energy Consumption for Day 8: {prediction[0]:.2f}")

# Save the model
joblib.dump(model, "models/energy_forecasting_model.pkl")

print("Model saved successfully!")
