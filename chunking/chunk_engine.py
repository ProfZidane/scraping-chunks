from langchain.text_splitter import RecursiveCharacterTextSplitter

import re

def clean_text(text):        
    cleaned_text = re.sub(r'\s+', ' ', text)
        
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text


def get_text_chunks(documents, chunk_size):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=200)
    chunks = []
    for doc in documents:
        chunks.extend(text_splitter.split_text(doc.page_content))
    
    return chunks


def save_large_chunks(documents, chunk_size, max_files=100):
    chunks = get_text_chunks(documents, chunk_size)        
    cleaned_chunks = [clean_text(chunk) for chunk in chunks]
    chunk_size = len(cleaned_chunks) // max_files + (len(cleaned_chunks) % max_files > 0)
    large_cleaned_chunks = [cleaned_chunks[i:i + chunk_size] for i in range(0, len(cleaned_chunks), chunk_size)]        
    
    print(f"{len(large_cleaned_chunks)} large chunks generated.")

    return large_cleaned_chunks