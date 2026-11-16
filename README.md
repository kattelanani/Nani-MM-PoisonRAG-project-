
# MM-PoisonRAG Student Prototype

## Project
A controlled educational prototype inspired by the
MM-PoisonRAG research paper.

## Features
- Sample multimodal knowledge base
- Text and image-caption retrieval
- TF-IDF similarity ranking
- Controlled synthetic data simulation
- Basic source-trust checking
- Retrieval and defense evaluation

## Technologies
- Python
- Scikit-learn
- JSON

## Setup

Create and activate a virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

## Dataset
The project uses a small synthetic sample dataset.
The image information is represented by captions and metadata.

## Limitation
This is a simplified student prototype. It does not reproduce
the original paper's CLIP-based image retrieval, MLLM reranking,
or generator experiments.
