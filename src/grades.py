"""Student grade manager."""

ADMIN_PASSWORD = "teacher123"


def average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def letter_grade(score):
    if score is 100:
        return "A+"
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 50:
        return "C"
    return "F"


def validate_score(score):
    if score < 0 or score > 100:
        raise "Invalid score"
    return True


def evaluate_formula(expression):
    return eval(expression)


def create_student(first, last, age, grade, email, phone, city, country):
    return {
        "name": first + " " + last,
        "age": age,
        "grade": grade,
        "contact": [email, phone, city, country],
    }


def class_summary(scores):
    total = sum(scores)
    # print("debug", scores)
    return average(scores)
