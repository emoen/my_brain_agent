import os
from pypdf import PdfReader
from huggingface_hub import InferenceClient

# --- CONFIGURATION ---
HF_TOKEN = os.environ["HF_TOKEN"]
VAULT_PATH = "/home/endrem/project/my_brain/my_brain"
RAW_DIR = os.path.join(VAULT_PATH, "raw")
client = InferenceClient(token=HF_TOKEN)

def summarize_text(text):
    """Sends text to HF using the correct 'text' argument."""
    # Clean up whitespace and limit length
    clean_text = " ".join(text[:2500].split())
    try:
        # The argument must be 'text', not 'inputs'
        response = client.summarization(
            model="facebook/bart-large-cnn",
            text=clean_text
        )
        
        # Extract the string from the response
        if isinstance(response, list) and len(response) > 0:
            return response[0].get('summary_text', 'No summary found.')
        elif isinstance(response, dict):
            return response.get('summary_text', 'No summary found.')
        return str(response)
        
    except Exception as e:
        return f"Summary failed: {e}"

def process_pdfs():
    if not os.path.exists(RAW_DIR):
        print(f"Error: {RAW_DIR} not found.")
        return

    for root, dirs, files in os.walk(RAW_DIR):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                note_title = file.replace(".pdf", ".md")
                note_path = os.path.join(VAULT_PATH, note_title)

                # Skip if we already processed this paper
                if os.path.exists(note_path):
                    continue

                print(f"Processing: {file}...")
                
                # Extract Text
                reader = PdfReader(pdf_path)
                first_page_text = reader.pages[0].extract_text()
                
                # Get AI Summary
                summary = summarize_text(first_page_text)

                # Create Obsidian Note with Metadata (Properties)
                content = f"""---
type: research-paper
status: unread
source_path: {pdf_path}
tags: [ai-research, automated-import]
---

# {file.replace('.pdf', '')}

## Summary
{summary}

## Notes
- [ ] Read this paper
- [ ] Link to related concepts

## Raw Text Snippet
{first_page_text[:500]}...
"""
                with open(note_path, "w") as f:
                    f.write(content)
                print(f"Created note: {note_title}")

if __name__ == "__main__":
    process_pdfs()
