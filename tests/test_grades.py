from src.grades import average, letter_grade, validate_score


def test_average():
    assert average([80, 90, 100]) == 90
    assert average([]) == 0


def test_letter_grade():
    assert letter_grade(100) == "A+"
    assert letter_grade(92) == "A"
    assert letter_grade(80) == "B"
    assert letter_grade(60) == "C"
    assert letter_grade(10) == "F"


def test_validate_score_ok():
    assert validate_score(50) is True
