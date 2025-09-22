import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1) Update path if your CSV is in a different location
CSV_PATH = "student_dataset_5000.csv"

print("Loading dataset from:", CSV_PATH)
df = pd.read_csv(CSV_PATH)

# Categorical columns present in CSVp
categorical_cols = [
    "FinancialCondition", "MaritalStatus",
    "FatherQualification", "MotherQualification",
    "MotherJobRole", "FatherJobRole",
    "Stream", "CourseName"
]

# Encode categorical columns with LabelEncoder and save encoders
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# Features & target
X = df[["Mid1", "Mid2", "EndSem", "Attendance"] + categorical_cols]
y = df["RiskLevel"]  # 'Low', 'Medium', 'High'

# Scale numeric features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Train RandomForest
model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
print("Training model...")
model.fit(X_train, y_train)

print("Train score:", model.score(X_train, y_train))
print("Test score :", model.score(X_test, y_test))

# Save artifacts
joblib.dump(model, "dropout_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(encoders, "encoders.pkl")

print("Saved: dropout_model.pkl, scaler.pkl, encoders.pkl")
