from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import time
import validators
import requests

def find_images(keyword, num_of_images = 5):
    base_url = f'https://www.instagram.com/explore/tags/{keyword}'

    # Can be replaced with any other driver
    driver = webdriver.Firefox()
    driver.get(base_url)

    # Giving time to Selenium to load the content
    time.sleep(6)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find_all('img')

    image_urls = []
    for img_tag in img_tags:
        img_url = img_tag['src']
        if len(image_urls) == num_of_images:
            break
        elif validators.url(img_url):
            image_urls.append(img_url)
        else:
            continue
    
    driver.quit()
    return image_urls

def download_image(image_url, path):
    image = requests.get(image_url, stream=True)

    with open(path, 'wb') as file:
        for chunk in image.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)