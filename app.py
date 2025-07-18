import os
import json
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ Missing GROQ_API_KEY. Add to .env or Streamlit Secrets.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Streamlit UI
st.set_page_config(page_title="JSON Extractor", page_icon="🔍")
st.title("🔍 AI JSON Extractor")

st.write("Paste unstructured text, and I'll extract **Name**, **Email**, and **Phone** as JSON.")

# Text input
user_text = st.text_area(
    "Paste your text here:",
    height=250,
    placeholder="Paste an email, resume, or paragraph..."
)

# Extract button
if st.button("Extract JSON"):
    if not user_text.strip():
        st.error("Please provide text for extraction.")
        st.stop()

    # Prompt for the model
    prompt = f"""
    Extract the following details from the text:
    - Name
    - Email
    - Phone number

    Return ONLY valid JSON in this format:
    {{
        "name": "...",
        "email": "...",
        "phone": "..."
    }}

    Text:
    {user_text}
    """

    with st.spinner("Extracting JSON..."):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                temperature=0,
                messages=[
                    {"role": "system", "content": "You extract structured data and output ONLY valid JSON."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content.strip()

            # Clean and parse model output
            def extract_json(text: str) -> dict:
                # Remove code fences and leading/trailing whitespace
                text = text.strip().replace("```json", "").replace("```", "")
                return json.loads(text)
            
            try:
                parsed_json = extract_json(result)
                st.subheader("✅ Extracted JSON")
                st.json(parsed_json)
            except json.JSONDecodeError:
                st.error("⚠️ The model returned invalid JSON after cleaning. Raw output below:")
                st.code(result, language="json")


        except Exception as e:
            st.error(f"Error: {e}")
