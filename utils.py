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

def chunk_text(text):
    pattern = r'(?=\n\d+\.\s)'

    sections = re.split(pattern, text)

    chunks = []

    for section in sections:
        section = section.strip()

        if len(section) > 50:
            chunks.append(section)

    return chunks