 # **🌟 ISRO HelpBot**

# ISRO_HelpBot

An AI-powered conversational assistant designed for information retrieval from ISRO's knowledge resources using a Knowledge Graph, Natural Language Processing (NLP), and semantic search. Built for the [ISRO Bharatiya Antariksh Hackathon 2025](https://www.isrohack.in/), this project aims to revolutionize access to space-related information.


## 🎯 Problem Statement (As per Hackathon)

The MOSDAC Portal hosts satellite data, documentation, and FAQs, but users face difficulty navigating its depth and diversity. This project introduces an AI-based HelpBot that addresses this issue by enabling intelligent, contextual, and interactive access to relevant information.

### 🧵 Objectives

- Build a virtual assistant using NLP/ML for intelligent question answering  
- Extract entities and relationships from structured/unstructured web content  
- Construct a dynamic knowledge graph for efficient information retrieval  
- Enable spatial intelligence for queries containing location-based terms  
- Ensure the system is modular, pip-installable, and deployable on other portals  

### 🎯 Expected Outcomes

- A chatbot capable of instant, contextual answers from MOSDAC content  
- A semantic knowledge graph modeling ISRO datasets and FAQs  
- CLI, Streamlit UI, and FastAPI API access  
- Packaged and deployable solution  

### 📏 Evaluation Parameters

- **Intent Recognition Accuracy**: Correct classification of user intent  
- **Entity Recognition Accuracy**: Accurate extraction of entities like satellite names, regions, and parameters  
- **Response Completeness**: Degree to which all relevant information is included in a response  
- **Response Consistency**: Logical coherence across multiple turns and related queries  



                                                                                     



## 📌 Features

-  **Query Understanding**: Extracts user intent and key entities using NLP and custom classifiers.
-  **Knowledge Graph Builder**: Dynamically parses structured and unstructured data into a semantic graph.
-  **Geospatial Intelligence**: Recognizes spatial entities like oceans, coordinates, and regions for spatially aware responses.
-  **Frontend Chat Interface**: Responsive UI built using **Tailwind CSS** and **Vanilla JS** for a lightweight, fast experience.
- ⚙️ **FastAPI Backend**: Handles real-time RESTful communication between UI and backend models.
-  **Evaluation Metrics**: Intent, entity, and answer quality tracked and visualized via automated tools.
-  **Pip-Installable Package**: Fully modular and installable via `pip install isro-helpbot`.

## 🗂️ Project Structure





```
ISRO HELPBOT/
├── __pycache__/                       # Compiled Python bytecode
├── .vscode/                           # VS Code settings for development
│   └── settings.json                  # Editor preferences and configurations
│
├── api/                               # FastAPI backend for handling API requests
│   ├── __pycache__/
│   ├── data/                          # API-level data files (temporary or static)
│   ├── static/                        # Static assets for FastAPI (CSS, JS, etc.)
│   ├── __init__.py                    # Marks directory as a Python package
│   ├── main_api.py                    # Uvicorn entrypoint with FastAPI app instance
│   ├── query_handler.py               # Logic to handle and respond to queries via API
│   └── routes.py                      # API endpoint definitions and routing
│
├── app/                               # Supplementary app scripts
│   ├── __pycache__/
│   └── main.py                        # Optional script for centralized app execution
│
├── core/                              # Chat logic and shared application functionality
│   ├── __pycache__/
│   └── chat_engine.py                 # Core engine handling conversations and message flow
│
├── data/                              # Datasets and documents used in KG construction
│   ├── clean_text/                    # Cleaned versions of raw text documents
│   ├── graph/                         # Serialized Knowledge Graphs
│   │   └── knowledge_graph.pkl        # Pickled NetworkX graph
│   ├── html/                          # Raw HTML files from scraped pages
│   ├── mosdac_docs/                   # Original documents (pdf/docx) from MOSDAC
│   ├── mosdac_pages/                  # Full saved MOSDAC HTML pages
│   └── raw_docs/                      # Raw document input before cleaning
│
├── raw_text/                          # Preprocessed plain text documents
│   ├── raw_docs                       # Raw text files for reference
│   └── test.text                      # Sample text used for testing
│
├── evaluation/                        # Evaluation scripts and outputs
│   ├── eval_engine.py                 # Script for evaluating intent/entity/response performance
│   └── results/                       # Output metrics and evaluation results
│       ├── intent_results.json        # JSON containing evaluation result details
│       ├── false_positives.csv        # Queries where intent classification failed
│       └── eval_summary.png           # Bar chart visualization of evaluation metrics
│
├── ingestion/                         # Document parsing and scraping modules
│   ├── docx_extractor.py              # Parse and extract text from .docx
│   ├── dynamic_scraper.py             # Scrape JavaScript-rendered MOSDAC pages
│   ├── html_scraper.py                # Parse static HTML files
│   └── pdf_extractor.py               # Extract content from PDFs
│
├── intent_classifier/                # Intent classification model and routing
│   ├── __pycache__/
│   ├── __init__.py                    # Package initializer
│   ├── intent_predictor.py            # ML model that predicts user intent
│   └── intent_router.py               # Maps intent labels to downstream task handlers
│
├── isro_helpbot/                      # Core pip-installable CLI module
│   ├── __pycache__/
│   ├── __init__.py                    # Package initializer
│   └── cli.py                         # CLI script to launch the bot via terminal
│
├── kg_builder/                        # Knowledge Graph construction modules
│   ├── entity_extractor.py            # Extracts named entities from documents/queries
│   ├── relationship_mapper.py         # Detects relationships among entities
│   ├── response_generator.py          # Forms responses from entities and graph traversal
│   └── text_preprocessor.py           # Cleans, splits and processes raw text
│
├── lib/                               # External shared libraries (if any)
│
├── model/                             # Models and vector storage
│   ├── __pycache__/
│   ├── embedding_generator.py         # Generates embeddings from textual input
│   ├── faiss_store_docs.pkl           # Serialized FAISS-compatible document store
│   ├── faiss_store.index              # FAISS binary index for fast semantic retrieval
│   ├── kg_reasoner.py                 # Reasoning logic using KG + LLM
│   ├── language_model.py              # Wrapper for local or API-based language models
│   ├── qa_pipeline.py                 # Complete pipeline from query to answer
│   └── vector_store.py                # Vector DB abstraction for FAISS, Chroma, etc.
│
├── tests/                             # Unit and integration test scripts
│   ├── test_intent_classifier.py      # Tests for intent classification logic
│   ├── test_kg.py                     # Tests for KG extraction and structure
│   └── test_scrapper.py               # Tests for scraping functions
│
├── ui/                                # Streamlit-based frontend
│   ├── __pycache__/
│   ├── components/                    # Streamlit component scripts (widgets, etc.)
│   ├── static/                        # Static images, graphs, etc.
│   ├── templates/                     # HTML templates (optional for hybrid UI)
│   ├── index.html                     # Frontend base page
│   ├── __init__.py                    # Marks UI as a package
│   └── streamlit_app.py               # Streamlit chatbot UI interface
│
├── venv/                              # Python virtual environment (excluded from Git)
├── .env                               # API keys and environment variables
├── .gitignore                         # Exclude rules for Git
├── build_index.py                     # Builds FAISS index for semantic search
├── config.py                          # Centralized configuration file (e.g., paths, thresholds)
├── entrypoints.py                     # Unified entrypoints for CLI/API/Streamlit
├── LICENSE                            # License file (MIT in this case)
├── main.py                            # Optional main runner script
├── MANIFEST.in                        # Include non-Python files during packaging
├── mosdac_crawler.py                  # Crawler script to fetch data from MOSDAC
├── pyproject.toml                     # Modern Python packaging metadata
├── requirements.txt                   # Required dependencies for pip install
└── setup.py                           # Package installer configuration
```




---

## ⚙️ Installation

```bash
pip install isro-helpbot
````

Or clone and run locally:

```bash
git clone https://github.com/Gaurav9693089415/ISRO-HelpBot.git
cd ISRO-HelpBot
pip install -e .
```

---

##  Usage

### 📍 Launch Chatbot UI

```bash
isro-helpbot
```

Runs Locally at  `http://localhost:8501/`.

### Launch FastAPI Backend

```bash
uvicorn api.main_api:app --reload --port 8080

```
Runs at http://localhost:8080/

---

## 📊 Evaluation Summary

| Metric                  | Score    |
|-------------------------|----------|
| ✅ Intent Recognition    | 100.00%  |
| 🧠 Entity Recognition    | 80.00%   |
| 📚 Response Completeness| 60.00%   |
| 🔁 Response Consistency | 100.00%  |

**Evaluation artifacts saved under:**

- `evaluation/results/intent_results.json`  
- `evaluation/results/false_positives.csv`  
- `evaluation/results/eval_summary.png` (bar chart)

---

## 📂 Supported Document Types

* `.txt` – Plain text files
* `.pdf` – Scanned and digital PDFs
* `.docx` – Microsoft Word
* `.xlsx` – Excel Sheets

Uploaded files auto-update the Knowledge Graph.

---

## 💻 Technologies Used

| Category         | Tools / Frameworks                             |
|------------------|------------------------------------------------|
| NLP/ML           | spaCy, NLTK, SentenceTransformers, Sklearn     |
| Vector Search    | FAISS, Transformers, PyTorch                   |
| Knowledge Graph  | NetworkX, PyVis                                |
| Frontend         | Tailwind CSS, Vanilla JS                       |
| Backend          | FastAPI, Uvicorn                               |
| Others           | LangChain, OpenAI API, Selenium                |
```




## 🛡️ License

MIT License. See `LICENSE` file.

---

## 🙌 Acknowledgement

Special thanks to **ISRO**, **IN-SPACe**, and **AICTE** for organizing the [Bharatiya Antariksh Hackathon 2025](https://www.isrohack.in/).

---

## ✨ Future Enhancements

* Voice interaction
* Image-based QnA using satellite maps

```


