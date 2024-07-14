import time
import concurrent.futures
import streamlit as st
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from helper import extract_features,extract_features_with_products
import time

def extract_features_with_spinner(func, pages, label):
    with st.spinner(label):
        return func(pages)
    
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


    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_basic = executor.submit(extract_features_with_spinner, extract_features, pages, "Extracting features with basic features")
        future_product = executor.submit(extract_features_with_spinner, extract_features_with_products, pages, "Extracting features with product details")
        
        d = future_basic.result()
        st.json(d)
        elapsed_time_basic = time.time() - start_time
        st.write(f"Time taken for extracting features with basic features: {elapsed_time_basic:.2f} seconds")
        
        d2 = future_product.result()
        st.json(d2)
        elapsed_time_product = time.time() - start_time
        st.write(f"Time taken for extracting features with product details: {elapsed_time_product:.2f} seconds")

    total_elapsed_time = time.time() - start_time
    st.write(f"Total time taken: {total_elapsed_time:.2f} seconds")
