import utils
print("CHUNK FUNCTION:", utils.chunk_text)

from utils import load_text, chunk_text

text = load_text("data/sample_text.txt")

chunks = chunk_text(text)

print("TOTAL CHUNKS:", len(chunks))

print("\n--- CHUNKS ---\n")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")

from utils import load_text, chunk_text

text = load_text("data/sample_text.txt")

print("RAW TEXT:\n", text)
print("\n--- SENTENCES ---")

import re
sentences = re.split(r'(?<=[.!?])\s+', text.strip())

for i, s in enumerate(sentences):
    print(i+1, s)