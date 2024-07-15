import concurrent.futures
import streamlit as st
import os
import tempfile
import time
import base64
from langchain_community.document_loaders import PyPDFLoader
from helper import extract_features, extract_features_with_products

st.set_page_config(layout="wide")
col1, col2 = st.columns([.5, .5])

def extract_features_with_spinner(func, pages, label):
    with st.spinner(label):
        return func(pages)
    
def displayPDF(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="width: 100%; height: 100vh;">"""

    st.markdown(pdf_display, unsafe_allow_html=True)

st.sidebar.title("Invoice Extraction")
st.sidebar.header("Upload Document")
uploaded_file = st.sidebar.file_uploader("Choose a file", type="pdf")

if uploaded_file is not None and st.sidebar.button("Extract Features"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    with col2:
        displayPDF(tmp_file_path)
    loader = PyPDFLoader(tmp_file_path)
    pages = loader.load_and_split()    
    with col1:
        with st.spinner("The Document parsing is under process"):
            start_time = time.time()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future_basic = executor.submit(extract_features_with_spinner, extract_features, pages, "Extracting features with basic features")
                future_product = executor.submit(extract_features_with_spinner, extract_features_with_products, pages, "Extracting features with product details")
                
                json_tab, text_tab = st.tabs(["Extracting features with basic features", "Extracting features with product details"])
                with json_tab:
                    d = future_basic.result()
                    st.json(d)
                    elapsed_time_basic = time.time() - start_time
                    st.write(f"Time taken for extracting features with basic features: {elapsed_time_basic:.2f} seconds")
                with text_tab:    
                    d2 = future_product.result()
                    st.json(d2)
                    elapsed_time_product = time.time() - start_time
                    st.write(f"Time taken for extracting features with product details: {elapsed_time_product:.2f} seconds")

    total_elapsed_time = time.time() - start_time
    st.write(f"Total time taken: {total_elapsed_time:.2f} seconds")
    
    # Cleanup temporary file
    os.remove(tmp_file_path)
