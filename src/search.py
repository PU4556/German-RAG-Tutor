import json
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# -----------------------------
# Load stored data
# -----------------------------
with open("storage/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

embeddings = np.load("storage/embeddings.npy")
embeddings = np.array(embeddings)

# -----------------------------
# User Query
# -----------------------------
query = input("Ask a question: ").strip().lower()

# IMPORTANT: improve retrieval quality with context hint
query = f"German grammar explanation: {query}"

# -----------------------------
# Create query embedding
# -----------------------------
query_embedding = model.encode(
    query,
    normalize_embeddings=True
)

# -----------------------------
# Similarity Search
# -----------------------------
scores = np.dot(embeddings, query_embedding)

# -----------------------------
# Top-K retrieval
# -----------------------------
top_k = 3
top_idx = np.argsort(scores)[::-1][:top_k]

best_index = top_idx[0]
best_score = scores[best_index]

# -----------------------------
# Debug output
# -----------------------------
print("\nDEBUG SCORES:")
for i, s in enumerate(scores):
    print(i, float(s))

print("\n" + "=" * 60)

# -----------------------------
# Threshold filtering
# -----------------------------
THRESHOLD = 0.30

if best_score < THRESHOLD:
    print("No relevant information found.")
else:
    print("TOP RESULTS:\n")

    for i in top_idx:
        print("=" * 60)
        print(chunks[i])
        print("Score:", float(scores[i]))

    print("\nBEST MATCH:\n")
    print(chunks[best_index])
    print(f"\nSimilarity Score: {best_score:.4f}")

print("=" * 60)