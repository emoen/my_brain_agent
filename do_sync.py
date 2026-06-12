import os
from pypdf import PdfReader
from huggingface_hub import InferenceClient

# --- CONFIGURATION ---
HF_TOKEN = os.environ["HF_TOKEN"]
VAULT_PATH = "/home/endrem/project/my_brain/my_brain"
RAW_DIR = "/home/endrem/project/my_brain/my_brain/raw/DivML"
client = InferenceClient(token=HF_TOKEN)

def get_full_summary(pdf_path):
    reader = PdfReader(pdf_path)
    all_summaries = []
    
    # We loop through the book in steps of 10 pages to find the "meat"
    # To read the *entire* thing, remove the [:5] slice, 
    # but be careful with API limits!
    for i in range(0, len(reader.pages), 10):
        text = reader.pages[i].extract_text()
        if len(text) < 200: continue # Skip empty/short pages
        
        clean_text = " ".join(text[:2500].split())
        try:
            print(f"  ...Summarizing section starting at page {i}")
            res = client.summarization(model="facebook/bart-large-cnn", text=clean_text)
            summary_text = res[0].get('summary_text', '') if isinstance(res, list) else res.get('summary_text', '')
            all_summaries.append(f"- Page {i}: {summary_text}")
        except Exception as e:
            print(f"  ! Skip page {i}: {e}")

    return "\n".join(all_summaries)

def process_pdfs():
    for root, dirs, files in os.walk(RAW_DIR):
        for file in files:
            if file.endswith(".pdf"):
                note_path = os.path.join(VAULT_PATH, file.replace(".pdf", ".md"))
                if os.path.exists(note_path): continue

                print(f"Deep Scanning: {file}...")
                full_insight = get_full_summary(os.path.join(root, file))

                content = f"""---
type: deep-research
source: {file}
---
# {file.replace('.pdf', '')}

## Comprehensive Insights
{full_insight}

## Links
- [[Research Index]]
"""
                with open(note_path, "w") as f:
                    f.write(content)

if __name__ == "__main__":
    process_pdfs()
