import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from utils import load_text, chunk_text

print("Loading embedding model...")
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Load text
text = load_text("data/sample_text.txt")

# Chunk text
chunks = chunk_text(text)

print(f"Created {len(chunks)} chunks")

# Create embeddings
embeddings = model.encode(chunks, normalize_embeddings=True)

# Ensure storage folder exists
os.makedirs("storage", exist_ok=True)

# Save chunks
with open("storage/chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)

# Save embeddings
np.save("storage/embeddings.npy", embeddings)

print("Ingestion completed successfully")
print("Chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)