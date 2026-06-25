from sentence_transformers import SentenceTransformer
from utils import load_text, chunk_text

print("Loading model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

text = load_text("data/sample_text.txt")

chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")

embeddings = model.encode(chunks)

print("\nEmbedding shape:")
print(embeddings.shape)

print("\nFirst embedding preview:")
print(embeddings[0][:10])