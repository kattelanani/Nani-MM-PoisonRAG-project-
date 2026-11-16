
import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RAGRetriever:
    def __init__(self, dataset_path="data/raw/knowledge_base.json"):
        self.dataset_path = Path(dataset_path)
        self.documents = []
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.document_vectors = None

        self.load_data()

    def load_data(self):
        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.dataset_path}"
            )

        with open(self.dataset_path, "r", encoding="utf-8") as file:
            self.documents = json.load(file)

        self.build_index()

    def build_index(self):
        combined_text = []

        for doc in self.documents:
            content = (
                doc.get("title", "") + " " +
                doc.get("text", "") + " " +
                doc.get("image_caption", "")
            )
            combined_text.append(content)

        self.document_vectors = self.vectorizer.fit_transform(
            combined_text
        )

    def search(self, query, top_k=3):
        if not query.strip():
            return []

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.document_vectors
        )[0]

        ranked_indices = scores.argsort()[::-1][:top_k]

        results = []

        for index in ranked_indices:
            document = self.documents[index].copy()
            document["score"] = float(scores[index])
            results.append(document)

        return results
