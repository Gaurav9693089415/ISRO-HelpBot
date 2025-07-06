import os
import fitz  # PyMuPDF

INPUT_DIR = "data/pdf"
OUTPUT_DIR = "data/raw_text"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_all_pdfs():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            full_path = os.path.join(INPUT_DIR, filename)
            text = extract_text_from_pdf(full_path)
            out_file = os.path.join(OUTPUT_DIR, f"{filename[:-4]}.txt")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"✅ Extracted: {out_file}")

if __name__ == "__main__":
    extract_all_pdfs()
