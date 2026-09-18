"""CIT105 Week 2 - QR Code Generator with CSV batch mode."""

import csv
import io
import zipfile
from urllib.parse import urlparse

import qrcode
import streamlit as st

from functions import safe_filename


def generate_qr(text, box_size=10, fill_color="black", border=4):
    """Generate and return a QR code image without using Streamlit."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)
    return qr.make_image(fill_color=fill_color, back_color="white")


def looks_like_malformed_url(text):
    """Return True when input looks like a URL but is malformed."""
    value = text.strip()
    if value.lower().startswith(("http://", "https://")):
        return not bool(urlparse(value).netloc)
    return value.lower().startswith(("www.", "http:", "https:"))


def read_batch_csv(csv_bytes):
    """Return valid rows and rejected-row messages from an uploaded CSV."""
    valid_rows = []
    rejected_rows = []

    try:
        text = csv_bytes.decode("utf-8-sig")
    except UnicodeDecodeError:
        return [], ["The file must be a UTF-8 CSV."]

    reader = csv.DictReader(io.StringIO(text))
    columns = {column.strip().lower() for column in (reader.fieldnames or [])}
    missing = [column for column in ("name", "url") if column not in columns]
    if missing:
        return [], [f"Missing required column(s): {', '.join(missing)}."]

    headings = {column.strip().lower(): column for column in reader.fieldnames}
    name_heading = headings["name"]
    url_heading = headings["url"]

    for row_number, row in enumerate(reader, start=2):
        try:
            name = (row.get(name_heading) or "").strip()
            url = (row.get(url_heading) or "").strip()
            if not name and not url:
                raise ValueError("name and URL are blank")
            if not name:
                raise ValueError("name is blank")
            if not url:
                raise ValueError("URL is blank")
            valid_rows.append({"row": row_number, "name": name, "url": url})
        except (AttributeError, TypeError, ValueError) as error:
            rejected_rows.append(f"Row {row_number}: {error}.")

    return valid_rows, rejected_rows


def build_batch_zip(rows, box_size=10, fill_color="black", border=4):
    """Build and return a ZIP containing one PNG for each valid CSV row."""
    zip_buffer = io.BytesIO()
    filename_counts = {}

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for row in rows:
            base_name = safe_filename(row["name"])
            filename_counts[base_name] = filename_counts.get(base_name, 0) + 1
            count = filename_counts[base_name]
            suffix = "" if count == 1 else f"_{count}"
            filename = f"{base_name}{suffix}.png"

            image = generate_qr(row["url"], box_size, fill_color, border)
            image_buffer = io.BytesIO()
            image.save(image_buffer, format="PNG")
            archive.writestr(filename, image_buffer.getvalue())

    return zip_buffer.getvalue()


def show_options():
    """Show QR appearance controls shared by both modes."""
    box_size = st.slider("Image size (box size)", 2, 20, 10)
    fill_color = st.color_picker("Foreground color", "#000000")
    border = st.slider("Border width", 1, 10, 4)
    return box_size, fill_color, border


def show_single_mode():
    """Display the original single-code workflow."""
    text = st.text_area(
        "Enter text or a URL",
        placeholder="Example: https://github.com",
        max_chars=500,
    )
    st.caption(f"Characters: {len(text)} / 500")
    box_size, fill_color, border = show_options()

    if text.strip() and looks_like_malformed_url(text):
        st.warning("This input looks like a URL, but it may be malformed.")

    if st.button("Generate QR Code"):
        if not text.strip():
            st.error("Please enter text or a URL. Input cannot be empty.")
            return
        image = generate_qr(text.strip(), box_size, fill_color, border)
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        png_data = buffer.getvalue()
        st.success("QR code generated successfully.")
        st.image(png_data, caption="Generated QR Code")
        try:
            filename_base = safe_filename(text.strip())[:50]
        except (TypeError, ValueError):
            filename_base = "qr_code"
        st.download_button("Download PNG", png_data, f"{filename_base}.png", "image/png")


def show_batch_mode():
    """Display CSV preview, validation results, and ZIP generation."""
    st.write("Upload a CSV with `name` and `url` columns.")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is None:
        st.info("Upload a CSV to preview its rows before generating QR codes.")
        return

    valid_rows, rejected_rows = read_batch_csv(uploaded_file.getvalue())
    col1, col2 = st.columns(2)
    col1.metric("Valid rows", len(valid_rows))
    col2.metric("Rejected rows", len(rejected_rows))

    if valid_rows:
        st.subheader("Valid row preview")
        st.dataframe(valid_rows, use_container_width=True, hide_index=True)
    if rejected_rows:
        st.subheader("Rejected rows and reasons")
        for message in rejected_rows:
            st.warning(message)
    if not valid_rows:
        st.error("No valid rows are available to generate.")
        return

    box_size, fill_color, border = show_options()
    if st.button("Generate Batch ZIP"):
        try:
            zip_data = build_batch_zip(valid_rows, box_size, fill_color, border)
        except (TypeError, ValueError) as error:
            st.error(f"The ZIP could not be created: {error}")
            return
        st.success(f"Created {len(valid_rows)} QR code(s).")
        st.download_button("Download ZIP", zip_data, "qr_codes.zip", "application/zip")


st.set_page_config(page_title="QR Code Generator", page_icon="📱")
st.title("QR Code Generator")
st.write("Create one QR code or generate a batch from a CSV file.")
mode = st.radio("Choose a mode", ("Single code", "Batch from CSV"), horizontal=True)
if mode == "Single code":
    show_single_mode()
else:
    show_batch_mode()
