def validate_non_empty_string(value: str) -> bool:
    """Validates that a string is not empty or just whitespaces."""
    return bool(value and str(value).strip())

def validate_positive_integer(value: str) -> bool:
    """Validates that a string can be cast to a positive integer."""
    try:
        val = int(value)
        return val > 0
    except ValueError:
        return False
