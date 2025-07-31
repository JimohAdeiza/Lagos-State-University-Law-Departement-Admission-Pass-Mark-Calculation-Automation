# LASU LAW ADMISSION CALCULATION SCRIPT (Optimized)
def get_grade(score):
    if 75 <= score <= 100:
        return 'A', 10
    elif 60 <= score <= 74:
        return 'B', 8
    elif 50 <= score <= 59:
        return 'C', 6
    elif 40 <= score <= 49:
        return 'D', 4
    elif 30 <= score <= 39:
        return 'E', 2
    elif 20 <= score <= 29:
        return 'F', 0
    else:
        return 'Undefined', 0

# JAMB Section
jamb_total_score = 240  # out of 400
jamb_score_converted = jamb_total_score / 8  # Scaled to 50%
print(f"JAMB Score (converted): {jamb_score_converted}")

# O'Level Subject Scores
subjects = {
    'English': 70,
    'Mathematics': 65,
    'Government': 75,
    'Literature': 68,
    'Economics': 60
}

# Calculate O'Level Grade Points
total_grade_points = 0
print("\nO'Level Grades & Points:")

for subject, score in subjects.items():
    grade, point = get_grade(score)
    total_grade_points += point
    print(f"{subject}: Score = {score}, Grade = {grade}, Point = {point}")

# Final Cutoff Calculation
final_score = jamb_score_converted + total_grade_points
print(f"\nTotal O'Level Grade Points: {total_grade_points}")
print(f"Final LASU Law Admission Score: {final_score}")

# Admission Decision
if 70 <= final_score <= 100:
    print("✅ Congratulations, you passed successfully!")
else:
    print("❌ Sorry, you did not meet the cutoff.")
