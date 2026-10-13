import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Sample IoT sensor data
data = {
    "Temperature": [30, 45, 60, 75, 90],
    "Vibration": [2, 3, 5, 7, 9],
    "Pressure": [100, 98, 95, 90, 85],
    "Failure": [0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Temperature", "Vibration", "Pressure"]]
y = df["Failure"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "models/predictive_maintenance_model.pkl")

# Test prediction
new_device = pd.DataFrame({
    "Temperature": [80],
    "Vibration": [8],
    "Pressure": [88]
})  
prediction = model.predict(new_device)

if prediction[0] == 1:
    print("⚠️ Warning: Device Failure Predicted!")
else:
    print("✅ Device is Operating Normally")

print("Model saved successfully!")
