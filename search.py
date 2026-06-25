import numpy as np
import json
from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Load stored data
chunks = json.load(open("storage/chunks.json", "r", encoding="utf-8"))
embeddings = np.load("storage/embeddings.npy")

query = input("Ask a question: ")

query_emb = model.encode([query], normalize_embeddings=True)[0]

scores = np.dot(embeddings, query_emb)

top_k = 3
top_idx = scores.argsort()[::-1][:top_k]

print("\nTOP RESULTS:\n")

for i in top_idx:
    print("=" * 50)
    print(chunks[i])
    print("Score:", float(scores[i]))