import streamlit as st
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from helper import extract_features,extract_features_with_products
import time
st.title("Invoice Extraction")
st.header("Upload Document")
uploaded_file = st.file_uploader("Choose a file", type="pdf")
if uploaded_file is not None and st.button("Extract Features"):
    with st.spinner("The Document parsing is under process"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        loader = PyPDFLoader(tmp_file_path)
        pages = loader.load_and_split()
        
        os.remove(tmp_file_path)

    start_time_basic = time.time()
    with st.spinner("Extracting features with basic features"):
        d = extract_features(pages)
        st.json(d)
    elapsed_time_basic = time.time() - start_time_basic
    st.write(f"Time taken for extracting features with basic features: {elapsed_time_basic:.2f} seconds")

    start_time_product = time.time()
    with st.spinner("Extracting features with product details"):
        d2 = extract_features_with_products(pages)
        st.json(d2)
    elapsed_time_product = time.time() - start_time_product
    st.write(f"Time taken for extracting features with product details: {elapsed_time_product:.2f} seconds")
