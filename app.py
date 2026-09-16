"""CIT105 Week 2 - QR Code Generator."""

import io
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

    image = qr.make_image(
        fill_color=fill_color,
        back_color="white",
    )

    return image


def looks_like_malformed_url(text):
    """Return True when input looks like a URL but is malformed."""
    value = text.strip()

    if value.lower().startswith(("http://", "https://")):
        parsed = urlparse(value)
        return not bool(parsed.netloc)

    if value.lower().startswith(("www.", "http:", "https:")):
        return True

    return False


st.set_page_config(
    page_title="QR Code Generator",
    page_icon="📱",
)

st.title("QR Code Generator")
st.write("Create and download a custom QR code.")

text = st.text_area(
    "Enter text or a URL",
    placeholder="Example: https://github.com",
    max_chars=500,
)

st.caption(f"Characters: {len(text)} / 500")

box_size = st.slider(
    "Image size (box size)",
    min_value=2,
    max_value=20,
    value=10,
    help="Range: 2 to 20 pixels per QR module.",
)

fill_color = st.color_picker(
    "Foreground color",
    value="#000000",
    help="Choose the foreground color of the QR code.",
)

border = st.slider(
    "Border width",
    min_value=1,
    max_value=10,
    value=4,
    help="Range: 1 to 10 modules.",
)

if text.strip() and looks_like_malformed_url(text):
    st.warning(
        "This input looks like a URL, but it may be malformed. "
        "You can still generate the QR code."
    )

if st.button("Generate QR Code"):
    if not text.strip():
        st.error("Please enter text or a URL. Input cannot be empty.")
    else:
        qr_image = generate_qr(
            text=text.strip(),
            box_size=box_size,
            fill_color=fill_color,
            border=border,
        )

        buffer = io.BytesIO()
        qr_image.save(buffer, format="PNG")
        png_data = buffer.getvalue()

        st.success("QR code generated successfully.")
        st.image(png_data, caption="Generated QR Code")

        try:
            filename_base = safe_filename(text.strip())[:50]
        except (TypeError, ValueError):
            filename_base = "qr_code"

        st.download_button(
            label="Download PNG",
            data=png_data,
            file_name=f"{filename_base}.png",
            mime="image/png",
        )
