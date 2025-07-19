from utils import evaluate_password

def test_weak_password():
    score, feedback = evaluate_password("1234")
    assert score < 20
    assert "Muy corta" in " ".join(feedback)

def test_strong_password():
    score, feedback = evaluate_password("T0d0_Est@_Bien2024")
    assert score >= 90
