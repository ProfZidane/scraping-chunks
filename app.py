from scraping.finding_urls import find_all_urls
from scraping.scraping_engine import get_web_page_content
from chunking.chunk_engine import get_text_chunks
from chunking.save_chunk_engine import save_on_disk


# Define the base urls
base_urls = [
    "https://www.eea.europa.eu/en/",
]

# find all urls
links = find_all_urls(base_urls, max_pages=50, limits=25)
print(links)

print()
print(" -------------------------------------------------------------- ")
print()

# Get all page contents
contents = get_web_page_content(links)
# print(contents)

# chunking the content
chunks = get_text_chunks(contents, chunk_size=1000)
save_on_disk(chunks, output_dir="data/scraped_chunks")

