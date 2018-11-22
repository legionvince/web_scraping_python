from bs4 import BeautifulSoup
import os
import re
import requests


def make_path():
    path = str(input("Enter a path: "))

    try:
        os.makedirs(path)
    except OSError:
        print("Creating directory failed.")
        make_path()
    else:
        print("Successfully created directory!")
    return path


def take_images():
    site = 'http://pixabay.com'

    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    urls = [img['src'] for img in img_tags]

    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        with open(filename.group(1), 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)


make_path()
take_images()
