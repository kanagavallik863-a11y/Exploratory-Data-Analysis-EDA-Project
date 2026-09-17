# Exploratory Data Analysis (EDA) Project

Analyzes a synthetic **Student Performance** dataset to uncover the patterns
and factors that most influence a student's final exam score.

## Project Structure

```
eda_project/
├── data/
│   ├── generate_data.py                  # Creates the synthetic dataset
│   └── student_performance.csv           # Dataset (500 rows, 10 columns)
├── notebooks/
│   └── eda_analysis.py                   # Full EDA pipeline
├── outputs/
│   └── eda_report.txt                    # Statistical summaries & key findings
├── visuals/
│   ├── correlation_heatmap.png
│   ├── pairplot.png
│   ├── final_score_distribution.png
│   ├── study_hours_vs_score.png
│   ├── attendance_vs_score.png
│   ├── score_by_parental_education.png
│   ├── score_by_extracurricular.png
│   └── score_by_gender.png
└── README.md
```

## How to Run

```bash
pip install pandas numpy matplotlib seaborn

python data/generate_data.py         # regenerate dataset (optional, already included)
python notebooks/eda_analysis.py     # run the full EDA
```

## Dataset

500 student records with numeric features (study hours, attendance, sleep,
prior score) and categorical features (gender, parental education,
extracurricular participation, study group), plus the target
`FinalExamScore`. The score was generated from a realistic combination of
these features plus random noise, so the patterns below reflect genuine
(not artificial) relationships.

## Methodology

1. **Data overview** — shape, column types, missing-value check (dataset is
   complete, no missing values).
2. **Statistical summary** — mean, std, quartiles for all numeric columns.
3. **Correlation analysis** — Pearson correlation of each numeric feature
   against `FinalExamScore`.
4. **Visual analysis** — correlation heatmap, pairplot, distribution plot,
   scatter plots with regression lines, and group comparisons (box/violin
   plots) across categorical variables.

## Key Findings

- **Study hours per day is the strongest predictor** of final exam score
  (correlation ≈ 0.61) — a clear positive linear relationship.
- **Prior academic score** is the second strongest factor (correlation ≈
  0.39), showing that past performance carries forward.
- **Attendance percentage** has a moderate positive relationship (correlation
  ≈ 0.22).
- **Sleep hours** shows almost no linear relationship with score in this
  dataset (correlation ≈ 0.04).
- Students who participate in **extracurricular activities** score
  marginally higher on average (61.3 vs 60.5).
- Average scores rise slightly with **parental education level**, with
  students whose parents hold a PhD scoring highest on average (63.2).

## Expected Outcome (Task Goal)

Demonstrates the EDA workflow: using statistical summaries and visualizations
to identify correlations and key influencing factors, then presenting the
findings in a structured, readable report.
