"""
generate_data.py
-----------------
Generates a synthetic "Student Performance" dataset for the
Exploratory Data Analysis project. Built-in correlations (study
hours, attendance, sleep, prior scores -> final exam score) give
the EDA real patterns to uncover.
"""

import numpy as np
import pandas as pd

np.random.seed(42)
N = 500

gender = np.random.choice(["Male", "Female"], N)
study_hours = np.round(np.random.normal(4, 1.8, N).clip(0, 10), 1)
attendance_pct = np.round(np.random.normal(80, 12, N).clip(40, 100), 1)
sleep_hours = np.round(np.random.normal(6.5, 1.2, N).clip(3, 10), 1)
prior_score = np.round(np.random.normal(65, 15, N).clip(20, 100), 1)
parental_education = np.random.choice(
    ["High School", "Bachelor's", "Master's", "PhD"], N, p=[0.35, 0.35, 0.22, 0.08]
)
extracurricular = np.random.choice(["Yes", "No"], N, p=[0.45, 0.55])
study_group = np.random.choice(["A", "B", "C"], N)

# Final exam score built from a realistic combination of the above
final_score = (
    5
    + 3.2 * study_hours
    + 0.20 * attendance_pct
    + 1.0 * sleep_hours
    + 0.30 * prior_score
    + np.where(extracurricular == "Yes", 2, 0)
    + np.random.normal(0, 7, N)
)
final_score = np.round(final_score.clip(0, 100), 1)

df = pd.DataFrame({
    "StudentID": [f"STU{3000+i}" for i in range(N)],
    "Gender": gender,
    "StudyHoursPerDay": study_hours,
    "AttendancePercent": attendance_pct,
    "SleepHours": sleep_hours,
    "PriorScore": prior_score,
    "ParentalEducation": parental_education,
    "Extracurricular": extracurricular,
    "StudyGroup": study_group,
    "FinalExamScore": final_score,
})

df.to_csv("/home/claude/eda_project/data/student_performance.csv", index=False)
print("Dataset generated:", df.shape)
print(df.describe())
