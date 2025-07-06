import os
import faiss
import pickle
import numpy as np

from model.embedding_generator import get_embedding

VECTOR_STORE_PATH = "model/faiss_store"
DATA_PATH = "data/clean_text"

def index_documents():
    docs = []
    embeddings = []

    for fname in os.listdir(DATA_PATH):
        if fname.endswith(".txt"):
            path = os.path.join(DATA_PATH, fname)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            docs.append((fname, content))
            embeddings.append(get_embedding(content).cpu().numpy())

    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    # Save FAISS index and documents
    faiss.write_index(index, f"{VECTOR_STORE_PATH}.index")
    with open(f"{VECTOR_STORE_PATH}_docs.pkl", "wb") as f:
        pickle.dump(docs, f)

    print(" Indexed and saved FAISS store.")

def search(query, top_k=3):
    index = faiss.read_index(f"{VECTOR_STORE_PATH}.index")
    with open(f"{VECTOR_STORE_PATH}_docs.pkl", "rb") as f:
        docs = pickle.load(f)

    query_vec = get_embedding(query).cpu().numpy().reshape(1, -1)
    scores, indices = index.search(query_vec, top_k)

    results = []
    for i in indices[0]:
        fname, doc = docs[i]
        results.append((fname, doc[:500]))  # Return doc snippet

    return results
