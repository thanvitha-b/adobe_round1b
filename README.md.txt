# Adobe Hackathon Round 1B – Persona-Based Document Intelligence

## 🧠 Task
Given multiple PDFs + a persona + job-to-be-done, extract and rank the most relevant document sections.

## 📥 Input
- `input/persona.json`: includes persona + job
- `input/*.pdf`: documents

## 📤 Output
- `output/output.json`: ranked list of key sections

## 🐳 Docker
```bash
docker build --platform linux/amd64 -t doc-analyzer:v1 .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none doc-analyzer:v1
