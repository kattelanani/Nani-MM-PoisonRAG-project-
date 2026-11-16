
def check_document(document):
    reasons = []

    if document.get("trusted") is not True:
        reasons.append("Source is not marked as trusted")

    if document.get("simulated") is True:
        reasons.append("Record is part of the synthetic simulation")

    if not document.get("source"):
        reasons.append("Source information is missing")

    if not document.get("text", "").strip():
        reasons.append("Document text is empty")

    if reasons:
        return {
            "status": "FLAGGED",
            "reasons": reasons
        }

    return {
        "status": "ACCEPTED",
        "reasons": []
    }


def filter_documents(documents):
    accepted = []
    flagged = []

    for document in documents:
        result = check_document(document)

        document["defense_status"] = result["status"]
        document["defense_reasons"] = result["reasons"]

        if result["status"] == "ACCEPTED":
            accepted.append(document)
        else:
            flagged.append(document)

    return accepted, flagged


def evaluate_dataset(documents):
    accepted, flagged = filter_documents(documents)

    total = len(documents)

    print("\n========== DEFENSE EVALUATION ==========")
    print("Total documents:", total)
    print("Accepted documents:", len(accepted))
    print("Flagged documents:", len(flagged))

    if total:
        acceptance_rate = len(accepted) / total * 100
        flagged_rate = len(flagged) / total * 100

        print("Acceptance rate:", round(acceptance_rate, 2), "%")
        print("Flagged rate:", round(flagged_rate, 2), "%")

    print("\nFlagged document details:")

    for document in flagged:
        print("\nID:", document["id"])
        print("Title:", document["title"])
        print("Reasons:", document["defense_reasons"])

    return accepted, flagged
