from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_text_chunks(documents, chunk_size):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=200)
    chunks = []
    for doc in documents:
        chunks.extend(text_splitter.split_text(doc.page_content))
    
    return chunks


def save_large_chunks(documents, chunk_size, max_files=100):
    chunks = get_text_chunks(documents, chunk_size)        
    
    chunk_size = len(chunks) // max_files + (len(chunks) % max_files > 0)
    large_chunks = [chunks[i:i + chunk_size] for i in range(0, len(chunks), chunk_size)]        
    
    print(f"{len(large_chunks)} large chunks generated.")

    return large_chunks