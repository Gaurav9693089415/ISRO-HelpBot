import os
import json
import csv

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from intent_classifier.intent_router import classify_intent


# Sample evaluation queries
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

# Ensure results directory exists
results_dir = os.path.join("evaluation", "results")
os.makedirs(results_dir, exist_ok=True)

print("\n Running Evaluation Tests:\n")

correct = 0

for query, expected in test_cases:
    predicted = classify_intent(query)
    is_correct = (predicted == expected)

    print(f"{'✓' if is_correct else '✗'} Query: {query}")
    print(f"    → Expected: {expected}, Got: {predicted}")

    results.append({
        "query": query,
        "expected": expected,
        "predicted": predicted,
        "correct": is_correct
    })

    if not is_correct:
        false_positives.append({
            "query": query,
            "expected": expected,
            "predicted": predicted
        })

    if is_correct:
        correct += 1

accuracy = correct / len(test_cases)
print(f"\n Intent Accuracy: {correct}/{len(test_cases)} ({accuracy:.2%})")

# Save full results to JSON
with open(os.path.join(results_dir, "intent_results.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

# Save false positives to CSV
with open(os.path.join(results_dir, "false_positives.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["query", "expected", "predicted"])
    writer.writeheader()
    writer.writerows(false_positives)

print(f"\n[✓] Results saved to: {results_dir}/intent_results.json and false_positives.csv")
