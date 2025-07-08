import os
import json
import csv
import sys
import difflib

# Add parent directory to path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from intent_classifier.intent_router import classify_intent
from kg_builder.entity_extractor import extract_entities
from kg_builder.response_generator import generate_response

# Sample evaluation queries with expected intents
test_cases = [
    ("What is INSAT-3D used for?", "info_query"),
    ("Download the latest ocean report", "download"),
    ("Where is SCATSAT located?", "location_query"),
    ("I want rainfall data for India", "data_request"),
    ("Okay, nothing specific", "fallback"),
    ("Explain Megha-Tropiques", "info_query"),
    ("Fetch satellite imagery for cyclone", "data_request"),
    ("Save document for weather data", "download"),
    ("Define INSAT", "info_query"),
    ("Which region does INSAT cover?", "location_query"),
]

results = []
false_positives = []

results_dir = os.path.join("evaluation", "results")
os.makedirs(results_dir, exist_ok=True)

print("\n🔍 Running Evaluation Tests:\n")

# Metric counters
correct_intent = 0
correct_entity = 0
complete_responses = 0
consistent_responses = 0

# Evaluate whether the response template matches the intent
def is_template_consistent(response_text, intent):
    if intent == "info_query":
        return "[Info]" in response_text
    elif intent == "location_query":
        return "[Location]" in response_text
    elif intent == "data_request":
        return "[Data Access]" in response_text
    elif intent == "download":
        return "[Download Link]" in response_text
    elif intent == "fallback":
        return "didn't understand" in response_text.lower()
    return False

# Evaluation loop
for query, expected_intent in test_cases:
    predicted_intent = classify_intent(query)
    entities = extract_entities(query)
    response = generate_response(predicted_intent, entities)

    response_text = response.get("answer", "")
    response_entities = response.get("entities", [])

    # Intent Recognition Accuracy
    is_intent_correct = (predicted_intent == expected_intent)
    if is_intent_correct:
        correct_intent += 1

    # Entity Recognition Accuracy
    is_entity_correct = any(
        ent[0].lower() in query.lower() for ent in response_entities
    )
    if is_entity_correct:
        correct_entity += 1

    # Response Completeness using fuzzy match
    is_response_complete = all(
        any(
            difflib.SequenceMatcher(None, ent[0].lower(), word).ratio() > 0.8
            for word in response_text.lower().split()
        )
        for ent in entities
    )
    if is_response_complete:
        complete_responses += 1

    # Response Consistency (template-based)
    is_consistent = is_template_consistent(response_text, predicted_intent)
    if is_consistent:
        consistent_responses += 1

    # Append result
    results.append({
        "query": query,
        "expected_intent": expected_intent,
        "predicted_intent": predicted_intent,
        "correct_intent": is_intent_correct,
        "correct_entity": is_entity_correct,
        "response_complete": is_response_complete,
        "response_consistent": is_consistent,
        "response": response_text,
        "entities": entities,
        "response_entities": response_entities
    })

    if not is_intent_correct:
        false_positives.append({
            "query": query,
            "expected": expected_intent,
            "predicted": predicted_intent
        })

# Final Evaluation Metrics
total = len(test_cases)
metrics = {
    "Intent Recognition Accuracy": round(correct_intent / total, 4),
    "Entity Recognition Accuracy": round(correct_entity / total, 4),
    "Response Completeness": round(complete_responses / total, 4),
    "Response Consistency": round(consistent_responses / total, 4)
}

# Print metrics to console
print("\n📊 Evaluation Summary:")
for key, value in metrics.items():
    print(f"   {key}: {value:.2%}")

# Save results
with open(os.path.join(results_dir, "intent_results.json"), "w", encoding="utf-8") as f:
    json.dump({"metrics": metrics, "details": results}, f, indent=4)

with open(os.path.join(results_dir, "false_positives.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["query", "expected", "predicted"])
    writer.writeheader()
    writer.writerows(false_positives)

print(f"\n✅ Results saved to: {results_dir}/intent_results.json and false_positives.csv\n")


import matplotlib.pyplot as plt

# Create directory for plots
plots_dir = os.path.join("evaluation", "plots")
os.makedirs(plots_dir, exist_ok=True)

# Plot metrics as bar chart
plt.figure(figsize=(8, 6))
plt.bar(metrics.keys(), [v * 100 for v in metrics.values()], color='skyblue')
plt.ylim(0, 100)
plt.ylabel('Percentage (%)')
plt.title('ISRO HelpBot Evaluation Metrics')
plt.xticks(rotation=30, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(metrics.values()):
    plt.text(i, v * 100 + 2, f"{v * 100:.1f}%", ha='center', fontweight='bold')

# Save as PNG
plot_path = os.path.join(plots_dir, "evaluation_summary.png")
plt.tight_layout()
plt.savefig(plot_path)
plt.close()

print(f"📈 Evaluation plot saved to: {plot_path}")
