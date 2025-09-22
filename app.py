import joblib
from flask import Flask, render_template
from flask_cors import CORS
import pandas as pd
import random

app = Flask(__name__)
CORS(app)

# Dataset load karo
df = pd.read_csv("student_dataset_5000.csv")

# Possible dropout reasons agar dataset me nahi mile toh
default_reasons = [
    "Low attendance",
    "Poor academic performance",
    "Financial issues",
    "Family problems",
    "Lack of interest in course",
    "Mental health challenges"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    # High risk students filter karo
    high_risk_students = df[df["RiskLevel"] == "High"]

    if high_risk_students.empty:
        return "⚠️ No high-risk students found in dataset!"

    # Ek random student select karo
    student = high_risk_students.sample(1).iloc[0].to_dict()

    # Attendance ko month-wise split kar dete hain (random breakdown)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    monthly_attendance = [max(40, min(100, int(student["Attendance"] + random.randint(-10, 10)))) for _ in months]

    # Student dict me extra details inject karte hain
    student["Months"] = months
    student["MonthlyAttendance"] = monthly_attendance

    # Dropout reason (agar dataset me hai toh use karo, warna random assign karo)
    if "Reason" in df.columns:
        student["Reason"] = student.get("Reason", random.choice(default_reasons))
    else:
        student["Reason"] = random.choice(default_reasons)

    # Phone number (agar dataset me hai toh use karo, warna dummy generate karo)
    if "PhoneNumber" in df.columns:
        student["PhoneNumber"] = student.get("PhoneNumber", f"+91{random.randint(6000000000, 9999999999)}")
    else:
        student["PhoneNumber"] = f"+91{random.randint(6000000000, 9999999999)}"

    return render_template("dashboard.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)
