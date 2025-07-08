from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import os
import sys

# Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
sys.path.append(PROJECT_ROOT)

from core.chat_engine import process_user_query, update_knowledge_graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# Mount UI paths
app.mount("/static", StaticFiles(directory=os.path.join(PROJECT_ROOT, "ui", "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(PROJECT_ROOT, "ui", "templates"))

chat_history = []

class QueryRequest(BaseModel):
    message: str

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "clean_text")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(req: QueryRequest):
    reply = process_user_query(req.message, chat_history)
    chat_history.append((req.message, reply))
    return {"response": reply}

@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    update_knowledge_graph(files, DATA_DIR)
    return JSONResponse(content={"message": "Knowledge Graph updated!"})

@app.post("/clear")
def clear_chat():
    chat_history.clear()
    return {"message": "Chat cleared"}
