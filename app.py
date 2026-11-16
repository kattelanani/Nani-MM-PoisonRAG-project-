
import json
import streamlit as st
from pathlib import Path
from PIL import Image

from src.retrieval.retriever import RAGRetriever
from src.defense.detector import check_document

st.set_page_config(
    page_title="MM-PoisonRAG",
    page_icon="🔍",
    layout="wide"
)

st.title("MM-PoisonRAG")
st.subheader("Multimodal Retrieval-Augmented Generation - Student Prototype")

st.info(
    "Research-inspired educational prototype for retrieval, "
    "controlled simulation and document trust evaluation."
)

DATA_PATH = Path("data/raw/knowledge_base.json")
SIMULATION_PATH = Path("data/processed/simulation_data.json")

def load_documents(path):
    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


tab1, tab2, tab3, tab4 = st.tabs([
    "Text Retrieval",
    "Image Upload",
    "Defense Evaluation",
    "Project Information"
])

with tab1:
    st.header("Knowledge Retrieval")

    query = st.text_input(
        "Enter your question",
        placeholder="What is solar energy?"
    )

    if st.button("Search Knowledge"):
        if query.strip():
            retriever = RAGRetriever()
            results = retriever.search(query)

            if results:
                for result in results:
                    with st.container(border=True):
                        st.subheader(result["title"])
                        st.write(result["text"])
                        st.write("Image description:",
                                 result.get("image_caption", "Not available"))
                        st.write("Source:", result.get("source"))
                        st.write(
                            "Similarity:",
                            round(result.get("score", 0), 3)
                        )
            else:
                st.warning("No results found.")
        else:
            st.warning("Please enter a question.")

with tab2:
    st.header("Image Upload and Inspection")

    uploaded_file = st.file_uploader(
        "Upload an educational image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption=uploaded_file.name,
            use_container_width=True
        )

        st.write("Filename:", uploaded_file.name)
        st.write("Image dimensions:", image.size)
        st.success("Image uploaded and loaded successfully.")

        st.caption(
            "This prototype displays uploaded images. "
            "Semantic image-text matching is not implemented yet."
        )

with tab3:
    st.header("Defense Evaluation")

    if st.button("Evaluate Dataset"):
        documents = load_documents(SIMULATION_PATH)

        if not documents:
            st.warning(
                "Simulation dataset not found. "
                "Run option 2 in main.py first."
            )
        else:
            accepted = []
            flagged = []

            for document in documents:
                result = check_document(document)

                if result["status"] == "ACCEPTED":
                    accepted.append(document)
                else:
                    flagged.append(document)

            total = len(documents)

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Documents", total)
            col2.metric("Accepted", len(accepted))
            col3.metric("Flagged", len(flagged))

            st.write(
                "Acceptance Rate:",
                f"{len(accepted) / total * 100:.2f}%"
            )

            st.write(
                "Flagged Rate:",
                f"{len(flagged) / total * 100:.2f}%"
            )

            st.subheader("Flagged Documents")

            if flagged:
                for document in flagged:
                    st.error(
                        f"{document['id']} - {document['title']}"
                    )
                    st.write(
                        check_document(document)["reasons"]
                    )
            else:
                st.success("No documents flagged.")

with tab4:
    st.header("About the Project")

    st.write("""
    MM-PoisonRAG is a student prototype inspired by research
    on security risks in Multimodal Retrieval-Augmented Generation.

    Features:
    - Text-based knowledge retrieval
    - Image upload and inspection
    - Controlled synthetic simulation
    - Document trust checking
    - Defense evaluation
    - Evaluation reports and graphs
    """)

    st.warning(
        "This is a simplified educational implementation, "
        "not an exact reproduction of the original research paper."
    )

    st.write("Dataset:", str(DATA_PATH))
    st.write("Simulation:", str(SIMULATION_PATH))

st.divider()
st.caption("MM-PoisonRAG | Student Research Implementation")
