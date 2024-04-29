import streamlit as st


# Configure Streamlit page settings
st.set_page_config(
    page_title="Text",
    page_icon = ":heartbeat:"
)


# Check if text is available in session state
if "TEXT" in st.session_state:
    # Retrieve text from session state
    text = st.session_state.TEXT

    # Display header indicating text content from PDF file
    st.header("Text content from your pdf file.")

    # Display text content within a styled container
    with st.container(border=True):
        # Apply custom CSS styling to the container
        st.markdown("""<style>
                    .my-container {
                    background-color: #000000;
                    padding: 30px;
                    }
                    </style>""", unsafe_allow_html=True)
        
        # Display text content within the styled container
        st.markdown(f"<div class='my-container'>{st.session_state['TEXT']}</div>", unsafe_allow_html=True)

else:
    # Prompt user to upload a PDF file if text is not available
    st.header("Please upload pdf file")
