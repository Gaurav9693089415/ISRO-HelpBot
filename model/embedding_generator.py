from sentence_transformers import SentenceTransformer

# Load the model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return model.encode(text, convert_to_tensor=True)
