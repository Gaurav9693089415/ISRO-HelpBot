import pickle
import os

# Load Knowledge Graph
def load_kg():
    kg_path = "data/graph/knowledge_graph.pkl"
    if not os.path.exists(kg_path):
        return None
    with open(kg_path, "rb") as f:
        return pickle.load(f)

# Answer using KG
def answer_with_kg(query: str):
    G = load_kg()
    if G is None:
        return ["Knowledge Graph not available."]

    matches = [node for node in G.nodes if query.lower() in node.lower()]
    if not matches:
        return ["No relevant info found in Knowledge Graph."]

    facts = []
    for match in matches:
        for u, v, data in G.edges(data=True):
            if u == match or v == match:
                facts.append(f"{u} --{data['relation']}--> {v}")
    return facts if facts else ["No relevant info found in Knowledge Graph."]
