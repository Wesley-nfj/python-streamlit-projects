import streamlit as st
import openai
import os

# Setting up API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(page_title="AI chatbot", layout="wide", page_icon="🤖")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# adding custom CSS for better look
st.markdown("""
    <style>
        .chat-message {
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .user-message {
            background-color: #DCF8C6;
            text-align: right;
        }
        .bot-message {
            background-color: #F1F0F0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🤖 Smart Assistant")
st.markdown("####  Hey, I am here to assist you. What can i help you with?")

# Input box
with st.container():
    
    with st.form(key="question_form", clear_on_submit=True):
        question = st.text_input("💬 Your question:", placeholder="What programing language should i learn first?")
        submit = st.form_submit_button("📤 Submit Question")

# submission stage
if submit and question.strip():
    # Save user's question to chat history
    st.session_state.messages.append({"role": "user", "content": question})

    # Display thinking spinner and get response
    with st.spinner("💭 Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a smart assistant."}] +
                         [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                temperature=0.5,
                max_tokens=600
            )
            answer = response['choices'][0]['message']['content'].strip()
            st.session_state.messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Display chat history
for message in reversed(st.session_state.messages):
    role = message["role"]
    content = message["content"]

    if role == "user":
        st.markdown(f'<div class="chat-message user-message"><strong>You:</strong><br>{content}</div>', unsafe_allow_html=True)
    elif role == "assistant":
        st.markdown(f'<div class="chat-message bot-message"><strong>STEM Tutor:</strong><br>{content}</div>', unsafe_allow_html=True)

# Footer effect
st.markdown("---")
st.markdown("© 2025 smart ai assistant | Built with ❤️ using [Streamlit](https://streamlit.io/) and [OpenAI GPT-3.5](https://platform.openai.com)")

