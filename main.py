# Import necessary libraries
import streamlit as st
from PyPDF2 import PdfReader 


# Configure Streamlit page settings
st.set_page_config(
    page_title = "Upload PDFs",
    page_icon = ":heartbeat:"
)

# Set API key in session state
st.session_state.API_KEY = "YOUR_API_KEY"

# Function to extract text from PDF file
def extract_text_from_pdf(file):
    """
    Extracts text from a PDF file.
    
    Parameters:
    - file: A file-like object representing the PDF file.
    
    Returns:
    - text (String): Extracted text from the PDF.
    """
    text = ""
    pdf_reader = PdfReader(file)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Upload PDF file
uploaded_file = st.file_uploader("Upload your PDF", type = ["pdf"], accept_multiple_files = False)
if uploaded_file:
    st.session_state["uploaded_file"] = uploaded_file
    st.session_state["TEXT"] = extract_text_from_pdf(st.session_state["uploaded_file"])

else:
    st.write("PDF is required...")

    


