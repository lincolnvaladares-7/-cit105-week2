# CIT105 Week 2 - QR Code Generator Specification

Student: Lincoln Guimaraes Valadares

## Application Name

QR Code Generator

## Purpose

The purpose of this application is to allow a user to enter text or a URL and generate a QR code that can be displayed on the screen and downloaded as a PNG image.

## User Interface

The application will use Streamlit.

The interface will contain:

- A text box for entering text or a URL.
- A visible character counter.
- A control for selecting QR image size.
- A control for selecting foreground color.
- A control for selecting border width.
- A Generate QR Code button.
- A generated QR code displayed on the page.
- A Download PNG button.

## Input

The user can enter normal text or a URL.

The application will reject:

- Empty input.
- Input containing only spaces.

The application will display an error message instead of crashing.

If the input appears to be a URL but is malformed, the application will display a warning but will still allow QR code generation.

## QR Code Options

### Image Size

The user can select a box size from 2 to 20 pixels.

### Foreground Color

The user can choose the QR code foreground color.

### Border Width

The user can select a border width from 1 to 10 modules.

## QR Code Generation

QR generation will be handled by a separate Python function.

The function will:

1. Accept the text, box size, foreground color, and border width as arguments.
2. Create the QR code using the qrcode library and Pillow.
3. Return the generated image.
4. Contain no Streamlit commands.

## Image Storage

The generated PNG will be stored in memory using io.BytesIO.

The application will not create a temporary image file on disk.

## Download Filename

The downloaded PNG filename will be based on the user's input.

The application will reuse safe_filename() from functions.py instead of creating another filename-cleaning function.

## Dependencies

The application will use:

- Python
- Streamlit
- qrcode
- Pillow

All required Python packages will be listed in requirements.txt.

## Testing

The application will be tested with:

- Normal text.
- A valid URL.
- Empty input.
- Whitespace-only input.
- A malformed URL.
- Different image sizes.
- Different foreground colors.
- Different border widths.

The generated QR code will also be tested using a phone camera to confirm that it scans correctly.
