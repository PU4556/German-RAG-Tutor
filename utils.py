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


def chunk_text(text, max_words=90, overlap=2):

    text = clean_text(text)

    # split better: sentence + numbering + punctuation aware
    sentences = re.split(r'(?<=[.!?])\s+|\s(?=\d+\.)', text)

    chunks = []
    current_chunk = []
    current_words = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        word_count = len(sentence.split())

        if current_words + word_count > max_words:
            chunks.append(" ".join(current_chunk))

            current_chunk = current_chunk[-overlap:]
            current_words = sum(len(s.split()) for s in current_chunk)

        current_chunk.append(sentence)
        current_words += word_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks