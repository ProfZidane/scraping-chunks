import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


def find_all_urls(base_url, max_pages=50, limits=5):
    links = []
    interation = 0
    for url in base_url:
      links.append(url)
      source_code = requests.get(url)
      soup = BeautifulSoup(source_code.content, 'lxml')

      for link in soup.find_all('a'):

          if interation == limits:
            break          

          if (link['href'].startswith("#") == False):
              if (link['href'].startswith("https://") == True):
                  links.append(link['href'])
              else:
                  full_url = urljoin(url, str(link["href"]))
                  # recursived call
                  links.append(full_url)
                  sublinks = find_all_urls([full_url])
                  links += sublinks
          else:
              print("Skip {} link".format(link['href']))

          interation += 1


      return links