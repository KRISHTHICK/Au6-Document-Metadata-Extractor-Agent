import json
from utils.ner import extract_entities
from utils.extractor import extract_text
from openai import OpenAI

def analyze_metadata(text, file_name, llm_api_key=None):
    metadata = {
        "file_name": file_name,
        "word_count": len(text.split()),
        "character_count": len(text),
        "summary": "",
        "entities": extract_entities(text),
    }

    if llm_api_key:
        openai = OpenAI(api_key=llm_api_key)
        prompt = f"Read this document and classify its type (e.g., resume, invoice, report), list key topics and generate a 3-line summary:\n{text[:3000]}"
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        metadata["llm_response"] = completion.choices[0].message.content.strip()
    
    return metadata
