import os
import random
import time
import requests

websites = [
    "http://www.google.com",
    "http://youtube.com",
    "http://yahoo.com",
    "https://www.subnetting.net",
    "http://tryhackme.com/",
    "https://github.com/",
    "https://mashable.com",
    "https://alwaysjudgeabookbyitscover.com/",
    "https://thatsthefinger.com",
    "https://theuselesswebsite.com",
    "https://Microsoft.com",
    "https://apple.com",
    "https://udemy.com"
]

x = 0
while x < 10:
    currentSite = random.choice(websites)
    site = requests.get(currentSite)
    print(site)
    print("GET : ", currentSite)
    time.sleep(10)
