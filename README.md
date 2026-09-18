# CIT105 Week 2 - QR Code Generator

Student: Lincoln Guimaraes Valadares

## Project Description

This project contains a reusable Python function library and a Streamlit QR code generator. The app supports one QR code at a time and batch generation from a CSV file.

## Running the App

1. Install the dependencies with `pip install -r requirements.txt`.
2. Start the app with `streamlit run app.py`.
3. Choose **Single code** or **Batch from CSV**.

## Single-Code Mode

Enter text or a URL, choose the QR-code appearance, and select **Generate QR Code**. The generated PNG is displayed and can be downloaded.

## Batch Mode

Choose **Batch from CSV** and upload a UTF-8 CSV containing these columns:

```csv
name,url
Opening Session,https://example.com/opening
Lincoln Valadares,https://example.com/lincoln
```

Before generating, the app shows the valid count, rejected count, valid-row preview, and a reason for every rejected row. Blank names, blank URLs, whitespace-only rows, and files missing a required column are rejected without stopping the app.

Select **Generate Batch ZIP** to create one PNG per valid row and download all images in one ZIP file. Filenames are cleaned with `safe_filename()`. Duplicate names receive `_2`, `_3`, and later counters instead of overwriting previous files.

The committed `sample_batch.csv` includes valid rows, a duplicate name, and at least two rows that are intentionally rejected.

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
- `app.py` - Streamlit app with single and batch QR-code modes.
- `sample_batch.csv` - Example upload containing valid and rejected rows.
- `README.md` - Documents the project and functions.

## Input Validation

The functions validate input before processing it. When appropriate, TypeError or ValueError is raised with a message explaining the problem. The library functions return their results instead of printing them.

## AI Use Disclosure

ChatGPT was used to assist with understanding the assignment, developing example code, and documentation. GitHub Copilot was not used.
