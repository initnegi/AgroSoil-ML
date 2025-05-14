import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('dataset/Crop_recommendation.csv')

# Features and labels
X = df[['N', 'P', 'K', 'ph']]
y = df['label']  # 'label' column contains crop names

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open('model/crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as crop_model.pkl")
