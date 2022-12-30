import requests
import time
import concurrent.futures


def get_image_url():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    image_url = response.json()['message']
    return image_url


def download_image(image_url):
    image_bytes = requests.get(image_url).content
    image_name = image_url.split('/')[-1]
    image_name = f"{image_name}"
    with open(image_name, 'wb') as image_file:
        image_file.write(image_bytes)
        print(f"{image_name} was downloaded...")


if __name__ == '__main__':
    start_time = time.perf_counter()

    # create an array of random image urls
    image_urls = []
    for i in range(10):
        image_urls.append(get_image_url())

    # synchronously
    # for image_url in image_urls:    # ~15s
    #     download_image(image_url)

    # asynchronously
    with concurrent.futures.ThreadPoolExecutor() as executor:   # ~10s
        future_results = executor.map(download_image, image_urls)

    end_time = time.perf_counter()
    print(f"Finished in {end_time-start_time}s")

