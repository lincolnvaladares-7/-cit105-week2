# CIT105 Week 2 - Function Library Exercise Set

Student: Lincoln Guimaraes Valadares

## Project Description

This project contains a small Python function library. Each function performs one specific task, returns its result, and validates incorrect input.

## Functions

### 1. celsius_to_fahrenheit(c)
- Takes: A numeric Celsius temperature.
- Returns: The temperature converted to Fahrenheit.
- Rejects: Non-numeric input with a TypeError.

### 2. line_total(price, qty)
- Takes: A numeric price and quantity.
- Returns: Price multiplied by quantity.
- Rejects: Non-numeric input and negative quantities.

### 3. initials(full_name)
- Takes: A person's full name as text.
- Returns: The uppercase initials of the name.
- Example: "Luis De Leon" returns "LDL".
- Rejects: Non-text input and an empty name.

### 4. is_valid_url(text)
- Takes: Text containing a possible URL.
- Returns: True for an HTTP/HTTPS URL or False otherwise.
- Rejects: Invalid or blank values by returning False.

### 5. truncate(text, limit=20)
- Takes: Text and an optional character limit.
- Returns: The original text or shortened text followed by "...".
- Rejects: Invalid text, non-integer limits, and negative limits.

### 6. safe_filename(text)
- Takes: Arbitrary text.
- Returns: Text converted into a safer filename without spaces, slashes, backslashes, or quotes.
- Rejects: Non-text input and empty text.

## Files

- `functions.py` - Contains the six required functions.
- `demo.py` - Imports and tests the functions using valid and invalid input.
- `README.md` - Documents the project and functions.

## Input Validation

The functions validate input before processing it. When appropriate, TypeError or ValueError is raised with a message explaining the problem. The library functions return their results instead of printing them.

## AI Use Disclosure

ChatGPT was used to assist with understanding the assignment, developing example code, and documentation. GitHub Copilot was not used.
