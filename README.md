# Invoice Entity Recognition System

## Overview
The Invoice Entity Recognition System is designed to efficiently extract key information from invoice documents using advanced machine learning models provided by OpenAI. This project leverages the power of Pydantic for function calling and data validation, ensuring robust and scalable application architecture. The output is structured in JSON format, making it easy to integrate and further process the extracted data.

## Features
- **Entity Recognition**: Automatically identifies and extracts critical data from invoices, such as dates, amounts, company names, and more.
- **OpenAI Integration**: Utilizes cutting-edge models from OpenAI for high accuracy in text recognition and entity extraction.
- **JSON Output**: Data extracted from invoices is returned in a clean, structured JSON format for easy use in various applications.
- **Streamlit Interface**: Includes a user-friendly web interface built with Streamlit, allowing for easy interaction and real-time processing of invoice documents.
- **Threading Support**: Enhanced performance with threading in Python to handle multiple processes efficiently.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip and virtualenv

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shyam-Sundar-7/Entity_recogntition
   cd Entity_recogntition
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the file:
     ```
     OPENAI_API_KEY='your_openai_api_key_here'
     ```

### Running the Application
You can run the application using one of the two provided Streamlit scripts:
- **main.py**: Standard version.
- **main2.py**: Uses threading for potentially improved performance.
- **main3.py**: Better UI with threading performance.

To run the application, execute one of the following commands:
```bash
streamlit run main.py
# or
streamlit run main2.py
# or
streamlit run main3.py
```

## Demo

streamlit run main2.py

[streamlit_demo](https://github.com/user-attachments/assets/198705d5-28db-4b83-90b8-8c270af06d4a)

streamlit run main3.py

[streamlit_demo2](https://github.com/user-attachments/assets/2877527e-0df9-42b2-a511-2bdc3eff5910)