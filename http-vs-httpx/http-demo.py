import time

import requests

urls = [
    'https://books.toscrape.com/catalogue/category/books_default_15/index.html',
    'https://books.toscrape.com/catalogue/category/books_default_15/page-2.html',
    'https://books.toscrape.com/catalogue/category/books_default_15/page-3.html',
    'https://books.toscrape.com/catalogue/category/books_default_15/page-4.html',
    'https://books.toscrape.com/catalogue/category/books_default_15/page-5.html',
    'https://books.toscrape.com/catalogue/category/books_default_15/page-6.html',
    'https://books.toscrape.com/catalogue/category/books_default_15/page-7.html',
    'https://books.toscrape.com/catalogue/category/books_default_15/page-8.html',
]

def fetch():
    results = [requests.get(url) for url in urls]
    print(results)
    return results

start = time.perf_counter()
fetch()
end = time.perf_counter()
print(f"Runtime: {end-start}s")
