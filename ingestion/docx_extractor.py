import os
from docx import Document

INPUT_DIR = "data/docx"
OUTPUT_DIR = "data/raw_text"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_docx(filename):
    doc = Document(filename)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

def extract_all_docx():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".docx"):
            full_path = os.path.join(INPUT_DIR, filename)
            text = extract_docx(full_path)
            out_file = os.path.join(OUTPUT_DIR, f"{filename[:-5]}.txt")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"✅ Extracted: {out_file}")

if __name__ == "__main__":
    extract_all_docx()
