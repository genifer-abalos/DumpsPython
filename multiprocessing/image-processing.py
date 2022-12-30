import time
from PIL import Image, ImageFilter  # pip install Pillow
import concurrent.futures


image_names = [
    "n02086910_5547.jpg",
    "n02093754_4213.jpg",
    "n02085620_9357.jpg",
    "n02086240_6898.jpg",
    "patterdale-terrier-287612805105275kBT.jpg",
    "20180706_194432.jpg",
    "IMG_5177.jpg",
    "jager-1.jpg",
    "n02089973_4084.jpg",
    "little1.jpg",
]

size = (1200, 1200)


def process_image(image_name):
    image = Image.open(image_name)
    image = image.filter(ImageFilter.GaussianBlur(15))

    image.thumbnail(size)
    image.save(f'processed_image/{image_name}')
    print(f'{image_name} was processed...')


if __name__ == '__main__':
    start_time = time.perf_counter()

    # using loop
    # for image_name in image_names:
    #     process_image(image_name)
    # Takes ~0.1856s

    # using ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:  # you can easily SWITCH this to ThreadPoolExecutor also
        executor.map(process_image, image_names) # executor map this will run process_image() for every item in image_names
    # Takes ~0.1742s

    end_time = time.perf_counter()
    print(f"Finished in {end_time - start_time}s")
