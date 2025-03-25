#Phishing Website Detector
#PWD Backend

import requests
import whois
import re
import sys
from datetime import datetime
from urllib.parse import urlparse

#getting url input

link=input("URL:")
if "http" in link:
     pass
else:
     print("-please enter an url that contains its protocol, ex: http://, https://")
     print("-program terminated")
     sys.exit()
linkdata = whois.whois(link)
#print(linkdata)

#creation date and current date, verify if the domain is older than a year

def whoisd():
        linkcd = linkdata["creation_date"]
        print(linkcd)
        #linkcd2 = linkcd[0]
        linkcd1 = linkcd.date()
        linkcd3 = linkcd1.year
        nowdt = datetime.now()
        nowdt1 = nowdt.date()
        nowdt2 = nowdt1.year
        sub = nowdt2 - linkcd3
        if sub >= 1:
            return True
        else:
            return False
    
if True and whoisd():
     print("-the domain creation date is older than a year")
else:
     print("-the domain creation date is lesser than a year")

#special char and long urls

def is_long_url(url, max_length=100):
    return len(url) > max_length

def has_special_characters(url):
    valid_pattern = r'^[a-zA-Z0-9\-._~:/?#[\]@!$&\'()*+,;=%]*$'
    return not re.match(valid_pattern, url)

def detect_url(durl):
     if is_long_url(durl) or has_special_characters(durl):
          return True
     
if True and detect_url(link):
     print("-a problametic url")
else:
     print("-url has no special characters or exceeds the max lenght 100")

#check for ssl protocol

def ssl_check(surl):
     https_pattern = r'^https:\/\/[a-zA-Z0-9\-._~:/?#[\]@!$&\'()*+,;=%]*$'
     return re.match(https_pattern, surl)

if True and ssl_check(link):
     print("-uses ssl protocol")
else:
     print("-does not use ssl protocol, not safe")