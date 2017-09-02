#!/usr/bin/env python
# @author = 01010011 01101000 01111001 01100001 01101101 01100001 01101100 
# date	  = 09/06/2017


"""This script downloads a random wallpaper from https://wallpapers.wallhaven.cc and set it as your home script wallpaper."""
import random
import shutil
import requests
from PIL import Image


while True:
    ran = random.randint(1,999999)
    url = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.jpg".format(ran)
    response = requests.get(url, stream=True)
    if response.status_code == 404 :
        url = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.png".format(ran)
        response = requests.get(url, stream=True)
        if response.status_code == 404 :
            continue
        else:
            with open('/home/shyamal/Personal/Wallpaper/wallpaper.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            im = Image.open("/home/shyamal/Personal/Wallpaper/wallpaper.png")
            rgb_im = im.convert('RGB')
            rgb_im.save('/home/shyamal/Personal/Wallpaper/wallpaper.jpg')
    else:
        with open('/home/shyamal/Personal/Wallpaper/wallpaper.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    print("Job Done!")
    break
