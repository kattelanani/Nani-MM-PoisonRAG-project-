
import json
from pathlib import Path


def create_simulation_dataset(
    input_path="data/raw/knowledge_base.json",
    output_path="data/processed/simulation_data.json"
):
    input_file = Path(input_path)
    output_file = Path(output_path)

    with open(input_file, "r", encoding="utf-8") as file:
        documents = json.load(file)

    # Synthetic test record for controlled evaluation.
    # It is labelled untrusted and is not real-world information.
    simulated_record = {
        "id": "SIM001",
        "title": "Synthetic Test Record",
        "text": "This is deliberately incorrect sample information "
                "created only to test retrieval reliability.",
        "image_caption": "Synthetic test image caption for evaluation.",
        "source": "Controlled Simulation",
        "trusted": False,
        "simulated": True
    }

    simulated_documents = documents + [simulated_record]

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(simulated_documents, file, indent=4)

    print("Controlled simulation dataset created.")
    print(f"Total records: {len(simulated_documents)}")
    print(f"Saved to: {output_file}")

    return str(output_file)
