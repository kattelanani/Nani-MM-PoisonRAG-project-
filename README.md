# MM-PoisonRAG: Multimodal Retrieval-Augmented Generation Security Prototype

A student research implementation inspired by the research paper **"MM-PoisonRAG: Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks."**

## Project Overview

Retrieval-Augmented Generation (RAG) retrieves relevant information from an external knowledge base to support context-aware responses.

However, untrusted or misleading information in a knowledge base can affect the reliability of retrieved results.

This project demonstrates a simplified approach to studying this problem through:

- TF-IDF-based document retrieval.
- Controlled synthetic knowledge-base simulation.
- Metadata-based document validation.
- Accepted and flagged document evaluation.
- An interactive Streamlit application.

**Note:** This is an educational prototype inspired by the research paper. It does not reproduce the original paper's Localized Poisoning Attack (LPA) or Globalized Poisoning Attack (GPA) algorithms.

## Research Paper

**Title:** MM-PoisonRAG: Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks

**Authors:** H. Ha et al.

**Research Paper:** https://arxiv.org/abs/2502.17832

**Published Version:** https://aclanthology.org/2026.acl-long.1558/

## Project Objectives

1. Understand the working of Retrieval-Augmented Generation.
2. Build a small educational knowledge base.
3. Implement document retrieval using TF-IDF and cosine similarity.
4. Simulate an untrusted knowledge-base record.
5. Develop a basic metadata-based validation mechanism.
6. Evaluate accepted and flagged documents.
7. Develop a simple web interface for demonstration.

## System Architecture

```text
       Educational Knowledge Base
                  |
                  v
          TF-IDF Retrieval
                  |
                  v
         Retrieved Documents
                  |
                  v
       Metadata-Based Validation
                  |
           +------+------+
           |             |
           v             v
      Accepted       Flagged
      Documents      Documents
           |             |
           +------+------+
                  |
                  v
           Evaluation
          Reports & Graphs
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Scikit-learn | TF-IDF and cosine similarity |
| Pandas | Data processing and evaluation |
| Matplotlib | Graph generation |
| Pillow | Image handling and preview |
| Streamlit | Interactive web application |
| JSON | Knowledge-base storage |
| Git and GitHub | Version control |

## Dataset Description

The project uses a manually prepared synthetic educational knowledge base.

It contains five trusted educational records:

- Solar Energy
- Wind Energy
- Water Cycle
- Plant Photosynthesis
- Human Heart

An additional synthetic record is created for controlled simulation.

The evaluation dataset therefore contains six records:

- Five trusted records.
- One simulated untrusted record.

## Main Modules

### 1. Document Retrieval

File: `src/retrieval/retriever.py`

Uses TF-IDF vectorization and cosine similarity to retrieve documents relevant to a user's text query.

### 2. Simulation Module

File: `src/poisoning/simulation.py`

Creates a controlled simulation dataset containing an additional record marked as untrusted.

### 3. Defense Module

File: `src/defense/detector.py`

Checks document metadata, trust status, source information, and text availability to classify records as accepted or flagged.

### 4. Evaluation Module

File: `src/defense/evaluation.py`

Calculates document counts and percentages and generates evaluation reports and graphs.

### 5. Image Retrieval Utility

File: `src/retrieval/image_retriever.py`

Provides image-file listing and filename-based matching. Semantic image retrieval is not currently implemented.

### 6. Streamlit Application

File: `app.py`

Provides an interactive interface with:

- Text Retrieval
- Image Upload and Preview
- Defense Evaluation
- Project Information

## Experimental Results

The recorded experiment was performed using six documents.

| Evaluation Metric | Result |
|---|---:|
| Total Documents | 6 |
| Accepted Documents | 5 |
| Flagged Documents | 1 |
| Acceptance Rate | 83.33% |
| Flagged Rate | 16.67% |

### Result Interpretation

The implemented validation mechanism accepted five trusted records and flagged one synthetic untrusted record.

These percentages describe the behavior of the prototype on its small controlled dataset. They should not be interpreted as general security accuracy or benchmark performance.

## Project Structure

```text
MM-PoisonRAG/
│
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── knowledge_base.json
│   └── processed/
│       └── simulation_data.json
│
├── models/
│
├── src/
│   ├── retrieval/
│   │   ├── retriever.py
│   │   └── image_retriever.py
│   │
│   ├── poisoning/
│   │   └── simulation.py
│   │
│   └── defense/
│       ├── detector.py
│       └── evaluation.py
│
├── results/
│   ├── evaluation_report.csv
│   └── figures/
│
├── tests/
│   ├── test_defense.py
│   └── test_retrieval.py
│
└── docs/
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/kattelanani/Nani-MM-PoisonRAG-project-.git
```

### Step 2: Open the Project Folder

```bash
cd Nani-MM-PoisonRAG-project-
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, normally:

```text
http://localhost:8501
```

### Step 6: Run the Evaluation

```bash
python -m src.defense.evaluation
```

### Step 7: Run Tests

```bash
python -m tests.test_defense
```

```bash
python -m tests.test_retrieval
```

## Limitations

- The dataset is small and synthetically prepared.
- Retrieval uses text and image-caption fields rather than actual image embeddings.
- The image-upload component provides image preview functionality.
- The defense mechanism uses basic metadata-based checks.
- The original LPA and GPA algorithms are not implemented.
- The project does not reproduce the complete multimodal experiments from the reference paper.

## Future Enhancements

- Integrate real image embeddings for multimodal retrieval.
- Increase dataset size and diversity.
- Implement semantic consistency checking between text and images.
- Add stronger document provenance and trust verification.
- Evaluate additional defense approaches on larger datasets.
- Compare TF-IDF with dense retrieval methods.
- Integrate a language model for answer generation.

## References

1. H. Ha et al., "MM-PoisonRAG: Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks," ACL, 2026. https://aclanthology.org/2026.acl-long.1558/

2. P. Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," NeurIPS, 2020. https://arxiv.org/abs/2005.11401

3. G. Salton, A. Wong, and C. S. Yang, "A Vector Space Model for Automatic Indexing," Communications of the ACM, 1975.

4. V. Karpukhin et al., "Dense Passage Retrieval for Open-Domain Question Answering," EMNLP, 2020. https://aclanthology.org/2020.emnlp-main.550/

## Author

**KATTELA NANI**

USN: 24BTLCL007

Branch: CSE-AIML

## GitHub Repository

https://github.com/kattelanani/Nani-MM-PoisonRAG-project-

---

*This project is an educational research prototype developed to demonstrate document retrieval, controlled simulation, and basic knowledge-base validation.*