
import json
import os
import matplotlib.pyplot as plt
import pandas as pd

from src.defense.detector import filter_documents


def run_evaluation():
    dataset_path = "data/processed/simulation_data.json"

    with open(dataset_path, "r", encoding="utf-8") as file:
        documents = json.load(file)

    accepted, flagged = filter_documents(documents)

    total = len(documents)
    accepted_count = len(accepted)
    flagged_count = len(flagged)

    acceptance_rate = accepted_count / total * 100 if total else 0
    flagged_rate = flagged_count / total * 100 if total else 0

    os.makedirs("results/figures", exist_ok=True)

    # Save evaluation results
    results = pd.DataFrame([
        {"Metric": "Total Documents", "Value": total},
        {"Metric": "Accepted Documents", "Value": accepted_count},
        {"Metric": "Flagged Documents", "Value": flagged_count},
        {"Metric": "Acceptance Rate (%)", "Value": acceptance_rate},
        {"Metric": "Flagged Rate (%)", "Value": flagged_rate}
    ])

    results.to_csv("results/evaluation_report.csv", index=False)

    # Graph 1: Document counts
    plt.figure()
    plt.bar(
        ["Accepted", "Flagged"],
        [accepted_count, flagged_count]
    )
    plt.title("Defense Evaluation - Document Counts")
    plt.ylabel("Number of Documents")
    plt.savefig("results/figures/document_counts.png")
    plt.close()

    # Graph 2: Percentages
    plt.figure()
    plt.bar(
        ["Accepted", "Flagged"],
        [acceptance_rate, flagged_rate]
    )
    plt.title("Defense Evaluation - Percentages")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.savefig("results/figures/defense_percentages.png")
    plt.close()

    print("\n===== EVALUATION COMPLETED =====")
    print(results.to_string(index=False))
    print("\nSaved:")
    print("results/evaluation_report.csv")
    print("results/figures/document_counts.png")
    print("results/figures/defense_percentages.png")


if __name__ == "__main__":
    run_evaluation()
