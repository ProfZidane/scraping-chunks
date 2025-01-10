import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


def find_all_urls(base_urls, max_pages=50, limits=5):
    links = set()
    stack = base_urls
    iteration = 0

    while stack and iteration < max_pages:
        url = stack.pop()
        if url not in links:
            links.add(url)
            try:
                # Obtenir le contenu de la page
                source_code = requests.get(url)
                soup = BeautifulSoup(source_code.content, 'lxml')

                for link in soup.find_all('a', href=True):
                    href = link['href']

                    # Ignorer les ancres (#)
                    if href.startswith("#"):
                        continue

                    # Résoudre les URLs absolues et relatives
                    full_url = href if href.startswith("http") else urljoin(url, href)

                    if full_url not in links and iteration < limits:
                        stack.append(full_url)
                        iteration += 1
            except Exception as e:
                print(f"Erreur lors de la récupération de {url}: {e}")

    return list(links)