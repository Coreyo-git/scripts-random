# A script for sending web requests, emulates http traffic on a network. 
# Setup for a WEP cracking project within two networks created.

# CTRL + C to stop script/process !!!

# Requirements:
#   Linux: python -m pip install requests

#   Windows: Install Python: https://www.python.org/downloads/windows/
#            Download pip.py a module mananger for python: https://bootstrap.pypa.io/get-pip.py
#            Navigate to the pip.py directory within your file system and install pip.py via cmd: python get-pip.py
import os
import random # Module for randomizing data.
import time # Module for adding a pause timer.
import requests # Module for HTTP Requests.

websites = [ #Stores a list of websites to access, append to add more.
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
# Infinite loop
x = 0
while x < 10:
    currentSite = random.choice(websites) # Assings the current site to a random choice from the website list.
    site = requests.get(currentSite) #Stores the HTTP response.
    print(site) # Prints the HTTP response code
    print("GET : ", currentSite) # Prints the current site
    time.sleep(10) # Time in seconds for how long to wait inbetween each request.
