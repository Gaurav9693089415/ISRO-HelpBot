# 🚀 ISRO HelpBot

An AI-powered conversational assistant designed for intelligent information retrieval from [MOSDAC](https://www.mosdac.gov.in) — ISRO’s Meteorological and Oceanographic Satellite Data portal. It uses a custom-built Knowledge Graph, NLP pipelines, semantic search, and a modular architecture to assist users in real-time with accurate, contextual responses.

Built for the [ISRO Bharatiya Antariksh Hackathon 2025](https://www.isrohack.in/), this project addresses real usability and information access challenges faced by MOSDAC users.

---

## 📌 Features

- 🔎 **Query Understanding**: Extracts user intent and key entities using NLP and custom classifiers.
- 🧠 **Knowledge Graph Builder**: Dynamically parses structured and unstructured data into a semantic graph.
- 🌍 **Geospatial Intelligence**: Recognizes spatial entities like oceans, coordinates, and regions for spatially aware responses.
- 💬 **Frontend Chat Interface**: Responsive UI built using **Tailwind CSS** and **Vanilla JS** for a lightweight, fast experience.
- ⚙️ **FastAPI Backend**: Handles real-time RESTful communication between UI and backend models.
- 📊 **Evaluation Metrics**: Intent, entity, and answer quality tracked and visualized via automated tools.
- 📦 **Pip-Installable Package**: Fully modular and installable via `pip install isro-helpbot`.

---

## 🗂️ Project Structure

\`\`\`bash
ISRO HELPBOT/
├── api/                    # FastAPI backend with query routing and serving
├── app/                    # Central runner script
├── core/                   # Core chat engine logic
├── data/                   # Cleaned, raw, and HTML-extracted data
├── raw_text/               # Plain text files (raw and sample)
├── evaluation/             # Evaluation metrics and result images
├── ingestion/              # Document parsers (PDF, DOCX, HTML)
├── intent_classifier/      # Intent prediction and routing logic
├── isro_helpbot/           # CLI entrypoint and base package
├── kg_builder/             # Knowledge Graph construction modules
├── model/                  # Embedding generators, KG reasoner, FAISS index
├── tests/                  # Unit tests for intent, KG, scraping
├── ui/                     # Frontend built using Tailwind CSS & Vanilla JS
├── venv/                   # Python virtual environment
├── .env                    # Environment variables
├── .gitignore              # Git ignore rules
├── build_index.py          # Vector index builder
├── config.py               # Global configuration
├── entrypoints.py          # Launch endpoints for CLI/Streamlit
├── LICENSE                 # MIT License
├── main.py                 # Main application runner
├── MANIFEST.in             # Non-code file declaration for packaging
├── mosdac_crawler.py       # Crawler for downloading data from MOSDAC
├── pyproject.toml          # PyPI metadata
├── requirements.txt        # Dependencies
└── setup.py                # Pip installation configuration
\`\`\`

---

## ⚙️ Installation

### 📦 Install via pip (published package)

\`\`\`bash
pip install isro-helpbot
\`\`\`

### 🔧 Or clone and install locally:

\`\`\`bash
git clone https://github.com/Gaurav9693089415/ISRO-HelpBot.git
cd ISRO-HelpBot
pip install -e .
\`\`\`

---

## 🚀 Usage

### ▶️ Launch Streamlit Chatbot UI

\`\`\`bash
isro-helpbot
\`\`\`

Runs locally at \`http://localhost:8501/\`

### ▶️ Launch FastAPI Backend

\`\`\`bash
uvicorn api.main_api:app --reload --port 8080
\`\`\`

Runs at \`http://localhost:8080/\`

---

## 📊 Evaluation Summary

| Metric                     | Score     |
|---------------------------|-----------|
| ✅ Intent Recognition      | 100.00%   |
| 🧠 Entity Recognition       | 80.00%    |
| 📚 Response Completeness    | 60.00%    |
| 🔁 Response Consistency     | 100.00%   |

Evaluation results are saved under:  
\`evaluation/results/intent_results.json\`,  
\`false_positives.csv\`, and  
\`eval_summary.png\` (bar chart).

---

## 📂 Supported Document Types

* \`.txt\` – Plain text files
* \`.pdf\` – Scanned/digital PDFs
* \`.docx\` – Microsoft Word documents
* \`.xlsx\` – Excel spreadsheets
* \`.html\` – Web pages (static or dynamic)

All uploaded content is parsed and indexed into the Knowledge Graph.

---

## 🎯 Problem Statement (As per Hackathon)

The [MOSDAC Portal](https://www.mosdac.gov.in) hosts satellite data, documentation, and FAQs, but users face difficulty navigating its depth and diversity. This project offers an AI-based HelpBot that:

**Objectives:**

- Build a virtual assistant using NLP/ML for intelligent question answering.
- Extract entities and relationships from structured/unstructured web content.
- Construct a dynamic knowledge graph for efficient information retrieval.
- Enable spatial intelligence for queries containing location-based terms.
- Ensure the system is modular, pip-installable, and deployable on other portals.

**Expected Outcomes:**

- A chatbot capable of instant, contextual answers from MOSDAC content.
- A semantic knowledge graph modeling ISRO datasets and FAQs.
- CLI, Streamlit UI, and FastAPI API access.
- Packaged and deployable solution.

**Evaluation Parameters:**

- **Intent Recognition Accuracy**: Correct classification of user intent.
- **Entity Recognition Accuracy**: How well entities like satellite names, regions, parameters are extracted.
- **Response Completeness**: Degree to which all relevant info is covered in an answer.
- **Response Consistency**: Logical coherence across multiple turns and queries.

---

## 💻 Technologies Used

| Category      | Tools / Frameworks                         |
|---------------|---------------------------------------------|
| NLP/ML        | spaCy, NLTK, SentenceTransformers, Sklearn |
| Vector Search | FAISS, Transformers, PyTorch               |
| Knowledge Graph | NetworkX, PyVis                          |
| Frontend      | Tailwind CSS, Vanilla JS                   |
| Backend       | FastAPI, Uvicorn                           |
| Others        | LangChain, OpenAI API, Selenium            |

---

## 🏁 Final Outcome

- ✅ Knowledge Graph built from scraped + uploaded content
- ✅ Modular NLP and semantic search engine
- ✅ Real-time chatbot interface via UI & API
- ✅ Packaged into a CLI and PyPI-ready module

---

## 🛡️ License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.

---

## 🙌 Acknowledgement

Special thanks to **ISRO**, **IN-SPACe**, and **AICTE** for organizing the [Bharatiya Antariksh Hackathon 2025](https://www.isrohack.in).

---

## ✨ Future Enhancements

- 🎙️ Voice-enabled interaction
- 🛰️ Image-based Q&A from satellite visuals
- 🌍 Live data integration (e.g., real-time satellite passes, weather)