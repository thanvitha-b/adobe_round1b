import os
import json
from utils import analyze_documents

INPUT_DIR = "/app/input" if os.path.exists("/app/input") else "input"
OUTPUT_DIR = "/app/output" if os.path.exists("/app/output") else "output"

persona_file = os.path.join(INPUT_DIR, "persona.json")
with open(persona_file, "r") as f:
    persona_info = json.load(f)

pdf_files = [os.path.join(INPUT_DIR, f) for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]

result = analyze_documents(pdf_files, persona_info)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "output.json"), "w") as f:
    json.dump(result, f, indent=2)
