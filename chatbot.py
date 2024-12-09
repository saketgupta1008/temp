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
    
    # Function to download chat history
    def download_chat_history(messages, file_format):
        if file_format == "json":
            chat_data = json.dumps(messages, indent=4)
            file_name = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        else:  # Default to plain text
            chat_data = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages])
            file_name = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        return chat_data, file_name

    # Download section in sidebar
    file_format = st.selectbox("Select Format", ["text", "json"], key="download_format")
    if st.button("Download", key="download_button"):
        chat_data, file_name = download_chat_history(st.session_state.messages, file_format)
        st.download_button(
            label="Download Chat",
            data=chat_data,
            file_name=file_name,
            mime="application/json" if file_format == "json" else "text/plain",
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
        role_style = "text-align: left; color: #2b6777;" if msg["role"] == "assistant" else "text-align: right; color: #4a4a4a;"
        st.markdown(
            f"<div class='chat-message' style='{role_style}'><b>{msg['role'].capitalize()}:</b> {msg['content']}</div>",
            unsafe_allow_html=True,
        )
