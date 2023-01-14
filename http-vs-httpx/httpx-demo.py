import time
import asyncio
import httpx

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


# define the function asynchronously
async def fetch():  # can be run concurrently
    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in urls]
        results = await asyncio.gather(*reqs)
    print(results)
    return results

start = time.perf_counter()
asyncio.run(fetch())
end = time.perf_counter()
print(f"Runtime: {end-start}s")