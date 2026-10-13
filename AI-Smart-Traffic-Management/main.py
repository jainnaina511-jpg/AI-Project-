import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier

# Sample traffic data
data = {
    "Vehicles": [50, 80, 120, 150, 200],
    "Average_Speed": [60, 50, 40, 30, 20],
    "Traffic_Signal": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Vehicles", "Average_Speed"]]
y = df["Traffic_Signal"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# New traffic data
new_traffic = pd.DataFrame({
    "Vehicles": [170],
    "Average_Speed": [25]
})

# Predict
prediction = model.predict(new_traffic)

if prediction[0] == 1:
    print("🚦 Green Signal Recommended")
else:
    print("🛑 Red Signal Recommended")

# Save the model
joblib.dump(model, "models/traffic_management_model.pkl")

print("Model saved successfully!")

