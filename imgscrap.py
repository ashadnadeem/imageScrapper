__author__ = "Ashad Nadeem Mahmudi"
__date__ = "7/17/2020"

import urllib.request as rq
from bs4 import BeautifulSoup
from PIL import Image
import re
import os

def getImg(url):
    html = rq.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    images_src = soup.find_all('img', {'src':re.compile('.jpg')})
    domain = re.match(r"^(.*\.[\w]*)/",url).group(1)
    images=[]
    for i,image in enumerate(images_src):
        if i > 10:
            break
        full_url = image['src']
        images.append(full_url)
    return images

def downImg(image_list):
    """Receives an input of list containing links and downloads them"""
    for i,image in enumerate(image_list):
        full_url = image_list[i]
        name = "image-{}.jpg".format(i+1)
        print("downloading {}...".format(name))
        rq.urlretrieve(full_url,name)
    print("Complete Successfully")

def resize(links):
    """Resizes the images to 400x400px Note:Quality is lost"""
    for i in range(len(links)):
        name = "image-{}.jpg".format(i + 1)
        image = Image.open(name)
        new_image = image.resize((400,400))
        new_image.save(name)
    print("Resize complete")
def makeDirectory():
    """This Function Makes a directory named 'Images' and switches to it"""
    directory = os.getcwd() + "\Images"
    try:
        os.mkdir(directory)
        print("images folder created")
    except FileExistsError:
        print("Directory Exists")
    os.chdir(directory)


makeDirectory()
links = getImg(url="https://www.freeimages.com/")
downImg(links)
resize(links)