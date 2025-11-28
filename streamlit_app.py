import streamlit as st
from back import process_image_and_extract_data   # your own function

st.title("VScan – Visiting Card Reader")

uploaded_file = st.file_uploader("Upload Visiting Card", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Card", use_column_width=True)

    with st.spinner("Extracting data..."):
        data = process_image_and_extract_data(uploaded_file)

    st.success("Extracted Data")
    st.write(data)

    if st.button("Save to Google Sheet"):
        save_to_sheet(data)
        st.success("Saved to Google Sheet!")
