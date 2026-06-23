from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):
    """
    Load a PDF and return LangChain documents.
    """

    loader = PyPDFLoader(pdf_path)

    return loader.load()

def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
import re

def split_sentences(text):
    # clean sentence splitting
    return re.split(r'(?<=[.!?])\s+', text.strip())


import re

def clean_text(text):
    # normalize line breaks
    text = text.replace("\n", " ")

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


import re

def chunk_text(text, chunk_size=5, overlap=2):
    # Step 1: split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    i = 0

    # Step 2: build overlapping chunks
    while i < len(sentences):
        chunk = sentences[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap

    return chunks