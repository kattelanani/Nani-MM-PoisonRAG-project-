
from src.defense.detector import check_document


def test_untrusted_document():
    document = {
        "id": "TEST001",
        "title": "Test Record",
        "text": "Synthetic test content",
        "source": "Controlled Simulation",
        "trusted": False,
        "simulated": True
    }

    result = check_document(document)

    assert result["status"] == "FLAGGED"
    print("PASS: Untrusted document detected.")
    print("Reasons:", result["reasons"])


def test_trusted_document():
    document = {
        "id": "TEST002",
        "title": "Trusted Record",
        "text": "Verified sample content",
        "source": "Verified Sample Dataset",
        "trusted": True
    }

    result = check_document(document)

    assert result["status"] == "ACCEPTED"
    print("PASS: Trusted document accepted.")


if __name__ == "__main__":
    test_untrusted_document()
    test_trusted_document()
