#!/usr/bin/env python
# coding: utf-8



from bs4 import BeautifulSoup
import requests

from tqdm import tqdm
import time
import math
import mimetypes

rep="y"
while rep=="y":

    query=str(input("Enter which product's picture do you want to save "))
    url="https://www.snapdeal.com/search"
    params={
        "keyword":query
    }
    r=requests.get(url,params=params)
    r.url
    soup=BeautifulSoup(r.content,features="html.parser")

    products = soup.findAll('div', attrs = {"class": "product-tuple-listing"})
 
    i=0

    for product in products:
        img_tag = product.find('img')
        if 'src' in img_tag.attrs:
            img = img_tag.attrs['src']
        else:
            img = img_tag.attrs['data-src']
        title = product.find('p', attrs = {"class": "product-title"}).text
        price = product.find('span', attrs = {"class": "product-price"}).text

        i+=1
        # print(img)
        url=img
        r2=requests.get(url,stream=True)
        extn=mimetypes.guess_extension(r2.headers["Content-Type"])
        print(extn)
        if extn != None:
            size=int(r2.headers["Content-Length"])
            # print(r2.headers["Content-Length"])
            my_chunk_kaa_size=1024
            no_of_iterations=math.ceil(size/my_chunk_kaa_size)
            with open("SnapdealPics/"+query+str(i)+str(extn),"wb") as file: # Write binary file mode
                for chunk in tqdm(r2.iter_content(chunk_size=my_chunk_kaa_size),total=no_of_iterations):
                    file.write(chunk)
        else:
            print("Either URL is wrong or some other error as from mimetypes, the returned value is None and not an extension")
    rep=input("Do you want to download another file? Type y/n ")




