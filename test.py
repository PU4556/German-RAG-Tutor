import utils

from utils import load_text, chunk_text

# Load text
text = load_text("data/sample_text.txt")

# Chunk text
chunks = chunk_text(text)

# Output
print("CHUNK FUNCTION:", chunk_text)
print("TOTAL CHUNKS:", len(chunks))

print("\n--- CHUNKS ---\n")

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")