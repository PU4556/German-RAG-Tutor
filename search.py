import numpy as np
from sentence_transformers import SentenceTransformer
from utils import load_text, chunk_text

print("Loading model...")
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

text = load_text("data/sample_text.txt")
chunks = chunk_text(text)

print("Total chunks:", len(chunks))

chunk_embeddings = model.encode(chunks, normalize_embeddings=True)

query = input("Ask a question: ")
query_embedding = model.encode([query], normalize_embeddings=True)[0]

# cosine similarity = dot product (because normalized)
scores = np.dot(chunk_embeddings, query_embedding)

# TOP-K instead of single answer
top_k = 3
top_indices = scores.argsort()[::-1][:top_k]

print("\nTOP RESULTS:\n")

for idx in top_indices:
    print("=" * 50)
    print(chunks[idx])
    print("\nScore:", float(scores[idx]))