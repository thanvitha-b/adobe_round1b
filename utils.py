import fitz  # PyMuPDF
import os
def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if 5 < len(text) < 100:
                        sections.append({
                            "document": os.path.basename(pdf_path),
                            "page": page_num,
                            "section_title": text,
                            "importance_rank": 0  # placeholder
                        })
    return sections

def analyze_documents(pdf_paths, persona_info):
    all_sections = []
    for path in pdf_paths:
        all_sections.extend(extract_sections(path))

    # Dummy scoring logic (replace with real ML or semantic search)
    job_keywords = persona_info.get("job", "").lower().split()
    for section in all_sections:
        match_score = sum(word.lower() in section["section_title"].lower() for word in job_keywords)
        section["importance_rank"] = match_score

    # Sort by importance
    all_sections = sorted(all_sections, key=lambda x: -x["importance_rank"])
    for i, sec in enumerate(all_sections):
        sec["importance_rank"] = i + 1  # re-rank from 1

    return {
        "metadata": {
            "persona": persona_info.get("persona"),
            "job": persona_info.get("job"),
            "documents": [os.path.basename(p) for p in pdf_paths]
        },
        "extracted_sections": all_sections[:10]  # top 10 sections
    }
