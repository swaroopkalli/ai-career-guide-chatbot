import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# --- 1. CONFIGURATION ---

try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error("Error: Could not initialize Gemini Client. Check your GEMINI_API_KEY.")
    st.stop()

# Set your model and system instruction here
MODEL_NAME = "gemini-2.5-flash" # Changed for broad compatibility; you can revert to gemini-3-pro-preview if you have access
SYSTEM_INSTRUCTION = """
**Role and Persona:** You are "The AI Career Guide," a friendly, optimistic, and highly informative digital counselor specializing in careers, education paths, and the role of Artificial Intelligence (AI) in various fields.
... (Paste the rest of your detailed prompt here)
"""

# --- 2. STREAMLIT INTERFACE SETUP ---
st.set_page_config(page_title="🤖 AI Career Guide Chatbot")
st.title("🤖 AI Career Guide Chatbot")
st.subheader("Your AI Assistant for Career Paths & the Future of Work")

# Initialize messages list in Streamlit's session_state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI Career Guide. I specialize in helping you discover career paths after 10th or 12th grade and how AI fits into them. What subject or career question can I help you with today?"}
    ]

# Display all messages from the session_state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 3. CORE API CALL FUNCTION (Using your provided logic) ---

def generate_stream_response(prompt_messages, system_instruction):
    """Generates the AI's streaming response using the provided Gemini code logic."""
    
    # 1. Convert Streamlit history into the Gemini contents format
    contents = [
        types.Content(
            role="user" if m["role"] == "user" else "model",
            parts=[types.Part.from_text(text=m["content"])]
        )
        for m in prompt_messages
    ]
    
    # 2. Configure Tools and System Instruction
    tools = [types.Tool(googleSearch=types.GoogleSearch())]
    generate_content_config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        # thinkingConfig: { thinkingLevel: "HIGH" }, # Removed this non-standard dict format
        tools=tools,
    )

    # 3. Call the streaming API
    response_stream = client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=contents,
        config=generate_content_config,
    )
    
    return response_stream

# --- 4. HANDLE USER INPUT ---
if user_prompt := st.chat_input("Ask a career question here..."):
    # Append user message to history
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    # Display user's message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Get and display the streaming response
    with st.chat_message("assistant"):
        # Display the response using Streamlit's stream capability
        placeholder = st.empty()
        full_response = ""
        
        # Pass the current history (st.session_state.messages) and system prompt
        response_stream = generate_stream_response(st.session_state.messages, SYSTEM_INSTRUCTION)
        
        # Read the stream chunks and display them
        for chunk in response_stream:
            full_response += chunk.text
            placeholder.markdown(full_response + "▌") # Added blinking cursor for effect
        
        placeholder.markdown(full_response)
        
    # Append full AI message to history for the next turn
    st.session_state.messages.append({"role": "assistant", "content": full_response})