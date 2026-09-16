"""Demo for the CIT105 Week 2 function library."""

from functions import (
    celsius_to_fahrenheit,
    line_total,
    initials,
    is_valid_url,
    truncate,
    safe_filename,
)


def test_function(description, function, *args):
    """Call a function and print its result or error message."""
    try:
        result = function(*args)
        print(description, ":", result)
    except (TypeError, ValueError) as error:
        print(description, ": REJECTED -", error)


print("CIT105 Week 2 Function Demo")
print("-" * 35)

# 1. Celsius to Fahrenheit
test_function("Valid temperature", celsius_to_fahrenheit, 25)
test_function("Invalid temperature", celsius_to_fahrenheit, "hot")

# 2. Line total
test_function("Valid line total", line_total, 10.00, 3)
test_function("Invalid line total", line_total, 10.00, -2)

# 3. Initials
test_function("Valid initials", initials, "Luis De Leon")
test_function("Invalid initials", initials, "   ")

# 4. URL
test_function("Valid URL", is_valid_url, "https://github.com")
test_function("Invalid URL", is_valid_url, "   ")

# 5. Truncate
test_function("Valid truncate", truncate, "This sentence is very long", 10)
test_function("Invalid truncate", truncate, "Hello", -1)

# 6. Safe filename
test_function("Valid filename", safe_filename, 'My "Project"/File')
test_function("Invalid filename", safe_filename, "   ")
