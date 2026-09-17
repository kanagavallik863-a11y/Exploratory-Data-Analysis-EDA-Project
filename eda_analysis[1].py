"""
eda_analysis.py
-----------------
Exploratory Data Analysis on the Student Performance dataset.
Produces statistical summaries, correlation analysis, and a set of
visualizations to uncover patterns and key influencing factors
behind FinalExamScore.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

DATA_PATH = "/home/claude/eda_project/data/student_performance.csv"
VIS_DIR = "/home/claude/eda_project/visuals"
OUT_DIR = "/home/claude/eda_project/outputs"

df = pd.read_csv(DATA_PATH)
report = []


def log(msg=""):
    print(msg)
    report.append(str(msg))


log("=== DATASET OVERVIEW ===")
log(f"Shape: {df.shape}")
log(f"\nColumn types:\n{df.dtypes}")
log(f"\nMissing values:\n{df.isna().sum()}")

log("\n=== STATISTICAL SUMMARY (numeric columns) ===")
log(df.describe().round(2))

numeric_cols = ["StudyHoursPerDay", "AttendancePercent", "SleepHours",
                 "PriorScore", "FinalExamScore"]

# --- Correlation matrix ---
corr = df[numeric_cols].corr()
log("\n=== CORRELATION WITH FinalExamScore ===")
log(corr["FinalExamScore"].sort_values(ascending=False).round(3))

plt.figure(figsize=(7, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap - Numeric Features")
plt.tight_layout()
plt.savefig(f"{VIS_DIR}/correlation_heatmap.png", dpi=150)
plt.close()

# --- Pairplot to visualize relationships ---
sample = df.sample(min(300, len(df)), random_state=1)
g = sns.pairplot(sample[numeric_cols], diag_kind="kde", plot_kws={"alpha": 0.5, "s": 20})
g.fig.suptitle("Pairwise Relationships Between Numeric Features", y=1.02)
g.savefig(f"{VIS_DIR}/pairplot.png", dpi=150)
plt.close("all")

# --- Distribution of FinalExamScore ---
plt.figure(figsize=(8, 5))
sns.histplot(df["FinalExamScore"], bins=25, kde=True, color="#2563eb")
plt.title("Distribution of Final Exam Scores")
plt.xlabel("Final Exam Score")
plt.tight_layout()
plt.savefig(f"{VIS_DIR}/final_score_distribution.png", dpi=150)
plt.close()

# --- Study Hours vs Final Score scatter ---
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="StudyHoursPerDay", y="FinalExamScore",
            scatter_kws={"alpha": 0.4}, line_kws={"color": "red"})
plt.title("Study Hours per Day vs Final Exam Score")
plt.tight_layout()
plt.savefig(f"{VIS_DIR}/study_hours_vs_score.png", dpi=150)
plt.close()

# --- Attendance vs Final Score scatter ---
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="AttendancePercent", y="FinalExamScore",
            scatter_kws={"alpha": 0.4}, line_kws={"color": "red"}, color="#059669")
plt.title("Attendance % vs Final Exam Score")
plt.tight_layout()
plt.savefig(f"{VIS_DIR}/attendance_vs_score.png", dpi=150)
plt.close()

# --- Final score by Parental Education ---
plt.figure(figsize=(8, 5))
order = ["High School", "Bachelor's", "Master's", "PhD"]
sns.boxplot(data=df, x="ParentalEducation", y="FinalExamScore", order=order,
            hue="ParentalEducation", palette="Set2", legend=False)
plt.title("Final Exam Score by Parental Education")
plt.tight_layout()
plt.savefig(f"{VIS_DIR}/score_by_parental_education.png", dpi=150)
plt.close()

# --- Final score by Extracurricular participation ---
plt.figure(figsize=(6, 5))
sns.violinplot(data=df, x="Extracurricular", y="FinalExamScore",
                hue="Extracurricular", palette="pastel", legend=False)
plt.title("Final Exam Score by Extracurricular Participation")
plt.tight_layout()
plt.savefig(f"{VIS_DIR}/score_by_extracurricular.png", dpi=150)
plt.close()

# --- Final score by Gender ---
plt.figure(figsize=(6, 5))
sns.boxplot(data=df, x="Gender", y="FinalExamScore", hue="Gender",
            palette="coolwarm", legend=False)
plt.title("Final Exam Score by Gender")
plt.tight_layout()
plt.savefig(f"{VIS_DIR}/score_by_gender.png", dpi=150)
plt.close()

# --- Key insights summary ---
log("\n=== KEY INSIGHTS ===")
top_corr = corr["FinalExamScore"].drop("FinalExamScore").abs().sort_values(ascending=False)
log(f"Strongest predictor of FinalExamScore: {top_corr.index[0]} "
    f"(corr = {corr['FinalExamScore'][top_corr.index[0]]:.3f})")

group_means = df.groupby("Extracurricular")["FinalExamScore"].mean().round(2)
log(f"\nAvg score - Extracurricular Yes vs No:\n{group_means}")

edu_means = df.groupby("ParentalEducation")["FinalExamScore"].mean().reindex(order).round(2)
log(f"\nAvg score by Parental Education:\n{edu_means}")

with open(f"{OUT_DIR}/eda_report.txt", "w") as f:
    f.write("\n".join(report))

print("\nAll visuals and report saved.")
