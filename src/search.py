import json
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# -----------------------------
# Load stored chunks & embeddings
# -----------------------------
with open("storage/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

embeddings = np.load("storage/embeddings.npy")

# -----------------------------
# User Query
# -----------------------------
query = input("Ask a question: ")

query_embedding = model.encode(
    [query],
    normalize_embeddings=True
)[0]

# -----------------------------
# Similarity Search
# -----------------------------
scores = np.dot(embeddings, query_embedding)

best_index = np.argmax(scores)
best_score = scores[best_index]

THRESHOLD = 0.25
print("\nDEBUG SCORES:")
for i, s in enumerate(scores):
    print(i, float(s))

print("\n" + "=" * 60)

if best_score < THRESHOLD:
    print("No relevant information found.")
else:
    print("Most Relevant Chunk:\n")
    print(chunks[best_index])
    print(f"\nSimilarity Score: {best_score:.4f}")

print("=" * 60)