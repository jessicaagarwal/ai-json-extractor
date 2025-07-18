import os
import json
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ Missing GROQ_API_KEY. Add to .env or Streamlit Secrets.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="Dynamic JSON Extractor", page_icon="🔍")
st.title("🔍 AI JSON Extractor")

st.write("Paste unstructured text and choose the fields you want in the output JSON.")

st.sidebar.header("⚙️ JSON Fields")
default_fields = ["Name", "Email", "Phone"]
fields_input = st.sidebar.text_area(
    "Enter fields (comma-separated):",
    value=", ".join(default_fields),
    help="Example: Name, Email, Phone, Address, Company"
)

# Convert to list
selected_fields = [f.strip() for f in fields_input.split(",") if f.strip()]

user_text = st.text_area(
    "Paste your text here:",
    height=250,
    placeholder="Paste an email, resume, or paragraph..."
)

if st.button("Extract JSON"):
    if not user_text.strip():
        st.error("Please provide text for extraction.")
        st.stop()

    # Build the JSON format dynamically
    json_schema = "{\n" + ",\n".join([f'    "{f.lower()}": "..."' for f in selected_fields]) + "\n}"

    # Build prompt
    prompt = f"""
    Extract the following details from the text:
    {", ".join(selected_fields)}

    Return ONLY valid JSON in this format:
    {json_schema}

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
                text = text.strip().replace("```json", "").replace("```", "")
                return json.loads(text)

            try:
                parsed_json = extract_json(result)
                st.subheader("✅ Extracted JSON")
                st.json(parsed_json)
            
                # ✅ Download JSON button
                json_str = json.dumps(parsed_json, indent=4)
                st.download_button(
                    label="⬇️ Download JSON",
                    data=json_str,
                    file_name="extracted_data.json",
                    mime="application/json"
                )

            except json.JSONDecodeError:
                st.error("⚠️ The model returned invalid JSON after cleaning. Raw output below:")
                st.code(result, language="json")

        except Exception as e:
            st.error(f"Error: {e}")
