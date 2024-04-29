import streamlit as st
from openai import OpenAI


# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat",
    page_icon = ":bot:"
)

# Initialize OpenAI client with API key from session state
client = OpenAI(api_key = st.session_state.API_KEY)

# Check if text is available in session state
if "TEXT" in st.session_state:
    # Retrieve text from session state
    Text = st.session_state["TEXT"]

    # Check if messages exist in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Iterate over messages in session state   
    for message in st.session_state.messages:
        # Display each message in the chat interface
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

     # Prompt user for Question input     
    if prompt := st.chat_input("What is up?"):
        # Append user input to session state messages
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user input in the chat interface
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response using OpenAI's chat API    
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": """your are expert at information present on internet and
                     good on understanting the text content and give a prefect answer for a question.
                     behave as polite assistant and be as friendly chatbot.
                     Importent instruction :-
                        - understand the text content and question.
                        - Give answers for questions only from given text.
                        - If the question not releated to given text then response should be 'Irrelavent question.'.
                        - do not generate your own output"""},
                    {"role": "user", "content" : f"text = {Text} and question = {prompt}"}
                    ],
                stream=True,
                )
            response = st.write_stream(stream)
         # Append assistant's response to session state messages   
        st.session_state.messages.append({"role": "assistant", "content": response})

# If text is not available in session state, prompt user to upload a PDF file
else:
    st.header("Please upload any pdf file.")