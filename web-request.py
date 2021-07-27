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
    "https://"
]

x = 10
while x < 10:
    currentSite = random.choice(websites)
    site = requests.get(currentSite)
    time.sleep(10)