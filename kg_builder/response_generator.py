# kg_builder/response_generator.py

def generate_response(intent, entities):
    """
    Dummy response generator for evaluation testing.
    Replace with real logic later.
    """
    if intent == "info_query":
        return f"[Info] {entities}"
    elif intent == "location_query":
        return f"[Location] {entities}"
    elif intent == "data_request":
        return f"[Data Access] {entities}"
    elif intent == "download":
        return f"[Download Link] {entities}"
    else:
        return "Sorry, I didn't understand your request."
