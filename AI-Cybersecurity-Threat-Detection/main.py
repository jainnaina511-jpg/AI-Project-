import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Sample cybersecurity data
data = {
    "Login_Attempts": [2, 5, 10, 15, 20],
    "Failed_Logins": [0, 1, 3, 5, 8],
    "Unusual_Traffic": [0, 0, 1, 1, 1],
    "Threat": [0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Login_Attempts", "Failed_Logins", "Unusual_Traffic"]]
y = df["Threat"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# New login attempt
new_login = pd.DataFrame({
    "Login_Attempts": [18],
    "Failed_Logins": [6],
    "Unusual_Traffic": [1]
})

# Predict
prediction = model.predict(new_login)

if prediction[0] == 1:
    print("⚠️ Cyber Threat Detected!")
else:
    print("✅ No Cyber Threat Detected")

# Save model
joblib.dump(model, "models/cybersecurity_model.pkl")

print("Model saved successfully!")
