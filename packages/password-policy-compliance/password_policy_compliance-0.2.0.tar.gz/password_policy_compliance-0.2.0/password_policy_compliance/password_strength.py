import re
from zxcvbn import zxcvbn

def calculate_password_strength(password: str) -> dict:
    """
    Calculate the strength of a password using both custom rules and zxcvbn.
    
    Args:
    password (str): The password to evaluate
    
    Returns:
    dict: A dictionary containing the password strength score, feedback, and crack time estimates
    """
    # Custom rules
    length_score = min(len(password) / 12, 1)  # Max score at 12 characters
    uppercase_score = 1 if re.search(r'[A-Z]', password) else 0
    lowercase_score = 1 if re.search(r'[a-z]', password) else 0
    digit_score = 1 if re.search(r'\d', password) else 0
    special_char_score = 1 if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) else 0
    
    custom_score = (length_score + uppercase_score + lowercase_score + digit_score + special_char_score) / 5
    
    # Zxcvbn score
    zxcvbn_result = zxcvbn(password)
    zxcvbn_score = zxcvbn_result['score'] / 4  # Normalize to 0-1 range
    
    # Combine scores (giving more weight to zxcvbn)
    combined_score = (custom_score + 2 * zxcvbn_score) / 3
    
    return {
        'score': round(combined_score * 100),  # Convert to 0-100 scale
        'feedback': zxcvbn_result['feedback'],
        'crack_times_display': zxcvbn_result['crack_times_display'],
        'crack_times_seconds': zxcvbn_result['crack_times_seconds'],
    }

def is_password_strong_enough(password: str, minimum_score: int = 50) -> bool:
    """
    Check if a password is strong enough based on a minimum score.
    
    Args:
    password (str): The password to evaluate
    minimum_score (int): The minimum score required (0-100)
    
    Returns:
    bool: True if the password is strong enough, False otherwise
    """
    strength_result = calculate_password_strength(password)
    
    # Adjust the threshold for considering a password strong enough
    adjusted_score = strength_result['score']
    
    # Boost score if password meets certain criteria
    if len(password) >= 10 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'\d', password):
        adjusted_score += 10
    
    return adjusted_score >= minimum_score

def get_crack_time_estimation(password: str) -> dict:
    """
    Get the estimated crack time for a password.
    
    Args:
    password (str): The password to evaluate
    
    Returns:
    dict: A dictionary containing crack time estimates
    """
    strength_result = calculate_password_strength(password)
    return {
        'crack_times_display': strength_result['crack_times_display'],
        'crack_times_seconds': strength_result['crack_times_seconds'],
    }
