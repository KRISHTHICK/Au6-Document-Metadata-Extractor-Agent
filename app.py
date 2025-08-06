import streamlit as st
import json
from agent.metadata_agent import analyze_metadata
from utils.extractor import extract_text

st.set_page_config(page_title="📄 Document Metadata Agent", layout="wide")
st.title("📊 Document Metadata Extractor Agent")

file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
llm_key = st.text_input("Optional: Enter OpenAI API Key for document type classification", type="password")

if file:
    text = extract_text(file)
    st.subheader("📖 Extracted Text Preview")
    st.text_area("Text", text[:2000])

    if st.button("🔍 Extract Metadata"):
        result = analyze_metadata(text, file.name, llm_api_key=llm_key if llm_key else None)
        st.json(result)

        with open(f"output/{file.name}_metadata.json", "w") as f:
            json.dump(result, f, indent=2)
