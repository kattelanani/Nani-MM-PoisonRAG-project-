
from src.retrieval.retriever import RAGRetriever
from src.poisoning.simulation import create_simulation_dataset
from src.defense.detector import filter_documents


def print_results(results):
    if not results:
        print("No matching documents found.")
        return

    for number, doc in enumerate(results, start=1):
        print(f"\nResult {number}")
        print("-" * 45)
        print("ID:", doc.get("id"))
        print("Title:", doc.get("title"))
        print("Text:", doc.get("text"))
        print("Image Caption:", doc.get("image_caption"))
        print("Source:", doc.get("source"))
        print("Similarity Score:", round(doc.get("score", 0), 3))


def main():
    print("=" * 55)
    print("       MM-PoisonRAG Student Prototype")
    print("=" * 55)

    print("\n1. Normal RAG retrieval")
    print("2. Run controlled simulation")
    print("3. Run defense evaluation")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            retriever = RAGRetriever()

            query = input("\nEnter your question: ")
            results = retriever.search(query)

            print("\nRetrieved Knowledge:")
            print_results(results)

        elif choice == "2":
            create_simulation_dataset()

            print("\nSimulation completed.")
            print("The synthetic record is labelled untrusted.")

        
        elif choice == "3":
            import json
            from src.defense.detector import evaluate_dataset

            with open(
                "data/processed/simulation_data.json",
                "r",
                encoding="utf-8"
            ) as file:
                documents = json.load(file)

            evaluate_dataset(documents)


        elif choice == "4":
            print("\nProgram closed.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
