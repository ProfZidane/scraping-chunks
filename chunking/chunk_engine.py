from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_text_chunks(documents, chunk_size):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=200)
    chunks = []
    for doc in documents:
        chunks.extend(text_splitter.split_text(doc.page_content))
    
    return chunks