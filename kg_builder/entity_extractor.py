import spacy
from kg_builder.text_preprocessor import preprocess_text


nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    text = preprocess_text(text)

    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
