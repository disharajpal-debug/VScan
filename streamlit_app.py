# vscan_streamlit.py
import os
import base64
from PIL import Image
from back import encode_image_to_base64, extract_details_with_gemini, append_to_master_sheet

import streamlit as st

st.title("VScan – Visiting Card Reader (Streamlit)")

uploaded_file = st.file_uploader("Upload Visiting Card", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Card", use_column_width=True)

    # Save uploaded file temporarily
    temp_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("Processing...")

    # Encode and extract using Gemini API
    image_base64 = encode_image_to_base64(temp_path)
    data = extract_details_with_gemini(image_base64)

    st.json(data)

    # Optional: remove temp file
    os.remove(temp_path)

    # Optional: Export to Google Sheet
    if st.button("Export to Google Sheet"):
        try:
            append_to_master_sheet(data)
            st.success("Exported successfully!")
        except Exception as e:
            st.error(f"Failed to export: {e}")
