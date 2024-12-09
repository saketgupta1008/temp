import streamlit as st
import json
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Confluence Chatbot", layout="wide")

# App Header with Branding
st.markdown("""
    <style>
    .main-header {
        font-size: 30px;
        font-weight: bold;
        color: #2b6777;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 16px;
        color: #4a4a4a;
        text-align: center;
    }
    .chat-message {
        font-size: 16px;
        line-height: 1.6;
        padding: 10px;
        margin: 5px 0;
        border-radius: 10px;
        max-width: 80%;
    }
    .user-message {
        background-color: #e6f7ff;
        border: 1px solid #80c9ff;
        text-align: right;
        margin-left: 20%;
    }
    .assistant-message {
        background-color: #f0f0f0;
        border: 1px solid #d1d1d1;
        text-align: left;
        margin-right: 20%;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Confluence Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Powered by LLM - Your EDP and ML Knowledge Assistant</div>', unsafe_allow_html=True)

# Initialize session state to hold chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for branding, download, and usage instructions
with st.sidebar:
    st.header("About Confluence Chatbot")
    st.write("""
    **Purpose**: Answer tech-related queries about the EDP department, ML topics, and team FAQs.
    
    ### Examples:
    - "What are the key ML initiatives in EDP?"
    - "Explain reinforcement learning in simple terms."
    - "How do I access the internal EDP Confluence page?"

    ---
    **Download Chat History**:
    """)

    # Function to prepare downloadable chat history
    def prepare_download(messages, file_format):
        if file_format == "json":
            chat_data = json.dumps(messages, indent=4)
            mime_type = "application/json"
            file_name = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        else:  # Plain text format
            chat_data = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages])
            mime_type = "text/plain"
            file_name = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        return chat_data, file_name, mime_type

    # Select format and trigger download
    file_format = st.selectbox("Select Format", ["text", "json"], key="download_format")
    if st.session_state.messages:  # Ensure there are messages to download
        chat_data, file_name, mime_type = prepare_download(st.session_state.messages, file_format)
        st.download_button(
            label=f"Download as {file_format.upper()}",
            data=chat_data,
            file_name=file_name,
            mime=mime_type,
        )

# Main chat container
st.write("### Chat Conversation")
chat_container = st.container()

# Input field for user query
with st.form("chat_input", clear_on_submit=True):
    user_input = st.text_input("Ask your query about EDP or ML:", "")
    submitted = st.form_submit_button("Send")

# Simulate an AI assistant response (replace this with LLM integration)
def generate_response(user_query):
    if "ML" in user_query or "machine learning" in user_query.lower():
        return "Machine Learning in EDP involves cutting-edge initiatives like reinforcement learning, generative AI, and anomaly detection pipelines."
    elif "EDP" in user_query.lower():
        return "The EDP department focuses on delivering scalable machine learning solutions for financial operations."
    else:
        return "I'm here to help with queries related to EDP and Machine Learning. Could you provide more details?"

# If the user submits a query, process it
if submitted and user_input:
    assistant_response = generate_response(user_input)
    # Update session state with the conversation
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Display chat messages
with chat_container:
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            st.markdown(
                f"<div class='chat-message user-message'><b>User:</b> {msg['content']}</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div class='chat-message assistant-message'><b>Assistant:</b> {msg['content']}</div>",
                unsafe_allow_html=True,
            )
