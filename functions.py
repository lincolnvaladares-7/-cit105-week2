"""Function library for CIT105 Week 2."""


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit and return the result."""
    if not isinstance(c, (int, float)) or isinstance(c, bool):
        raise TypeError("Temperature must be a number.")
    return (c * 9 / 5) + 32


def line_total(price, qty):
    """Return the total price for a quantity of items."""
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise TypeError("Price must be a number.")
    if not isinstance(qty, (int, float)) or isinstance(qty, bool):
        raise TypeError("Quantity must be a number.")
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    return price * qty


def initials(full_name):
    """Return the initials from a full name."""
    if not isinstance(full_name, str):
        raise TypeError("Full name must be text.")

    words = full_name.split()

    if not words:
        raise ValueError("Full name cannot be empty.")

    return "".join(word[0].upper() for word in words)


def is_valid_url(text):
    """Return True when text appears to be a valid HTTP or HTTPS URL."""
    if not isinstance(text, str):
        return False

    text = text.strip()

    if not text:
        return False

    return text.startswith(("http://", "https://"))


def truncate(text, limit=20):
    """Shorten text to the limit and add an ellipsis when shortened."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("Limit must be an integer.")
    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    if len(text) > limit:
        return text[:limit] + "..."

    return text


def safe_filename(text):
    """Return text converted into a safe filename."""
    if not isinstance(text, str):
        raise TypeError("Filename text must be a string.")

    text = text.strip()

    if not text:
        raise ValueError("Filename cannot be empty.")

    unsafe = ' /\\\'"'

    for character in unsafe:
        text = text.replace(character, "_")

    return text
