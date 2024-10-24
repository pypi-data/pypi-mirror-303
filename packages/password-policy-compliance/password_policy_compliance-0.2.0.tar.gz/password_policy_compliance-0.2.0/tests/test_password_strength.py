import pytest
from password_policy_compliance.password_strength import calculate_password_strength, is_password_strong_enough, get_crack_time_estimation

@pytest.mark.parametrize("password, expected_score_range", [
    ("weak", (0, 30)),
    ("Password123", (30, 60)),
    ("Str0ngP@ssw0rd!", (60, 100)),
])
def test_calculate_password_strength(password, expected_score_range):
    result = calculate_password_strength(password)
    assert 'score' in result
    assert expected_score_range[0] <= result['score'] <= expected_score_range[1]
    assert 'feedback' in result
    assert 'crack_times_display' in result
    assert 'crack_times_seconds' in result

@pytest.mark.parametrize("password, minimum_score, expected_result", [
    ("weak", 50, False),
    ("Password123", 50, True),
    ("Str0ngP@ssw0rd!", 80, True),
])
def test_is_password_strong_enough(password, minimum_score, expected_result):
    assert is_password_strong_enough(password, minimum_score) == expected_result

def test_get_crack_time_estimation():
    password = "Str0ngP@ssw0rd!"
    result = get_crack_time_estimation(password)
    assert 'crack_times_display' in result
    assert 'crack_times_seconds' in result
    assert 'online_throttling_100_per_hour' in result['crack_times_display']
    assert 'online_no_throttling_10_per_second' in result['crack_times_display']
    assert 'offline_slow_hashing_1e4_per_second' in result['crack_times_display']
    assert 'offline_fast_hashing_1e10_per_second' in result['crack_times_display']
