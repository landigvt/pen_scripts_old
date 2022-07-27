#!/usr/bin/env python

import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-l]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download = input("url: ")
print("download: {0}".format(download))
