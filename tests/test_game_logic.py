from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_check_guess_messages_too_high():
    # Test that the hint message for too high is correct (Go LOWER)
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "Go LOWER" in message

def test_check_guess_messages_too_low():
    # Test that the hint message for too low is correct (Go HIGHER)
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER" in message
