def convert_score_to_grade(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "C-"
    elif score >= 50:
        return "D"
    else:
        return "F"


def print_grade_summary(*, student_name, score, grade):

    print(f"Student {student_name} scored {score:.1f} → Grade: {grade}")



students = [
    {"name": "Zara", "score": 87.5},

    {"name": "Sadd", "score": 101}
]

for student in students:
    grade = convert_score_to_grade(student["score"])
    print_grade_summary(student_name=student["name"], score=student["score"], grade=grade)
