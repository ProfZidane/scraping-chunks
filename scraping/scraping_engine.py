from langchain_community.document_loaders import WebBaseLoader


def get_web_page_content(url):
    print("Loading page contents from {} URLs".format(len(url)))
    print()
    
    loader = WebBaseLoader(url)
    return loader.load()