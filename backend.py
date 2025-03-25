#Phishing Website Detector
#PWD Backend

import requests
import whois
import re
import sys
from datetime import datetime
from urllib.parse import urlparse
link=input("URL:")

def safe_check_url(link):
     flags = 0 # For percentage calculation
     Total_Checks = 3

     #getting url input


     
     linkdata = whois.whois(link)
     #print(linkdata)

     #creation date and current date, verify if the domain is older than a year

     def whoisd(flags):
               linkcd = linkdata["creation_date"]
               if isinstance(linkcd, list):
                    linkcd = linkcd[0]
               #print(linkcd)
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
    
     if True and whoisd(flags):
          flags += 1
          #print("-the domain creation date is older than a year")
     else:
          #print("-the domain creation date is lesser than a year")
          pass

     #special char and long urls

     def is_long_url(url, max_length=100):
          return len(url) > max_length

     def has_special_characters(url):
          valid_pattern = r'^[a-zA-Z0-9\-._~:/?#[\]@!$&\'()*+,;=%]*$'
          return not re.match(valid_pattern, url)

     def detect_url(durl,flags):
          if is_long_url(durl) or has_special_characters(durl):
               return True
     
     if True and detect_url(link,flags):
          pass
          #print("-a problametic url")
     else:
          #print("-url has no special characters or exceeds the max length 100")
          flags+=1
     #check for ssl protocol

     def ssl_check(surl):
          https_pattern = r'^https:\/\/[a-zA-Z0-9\-._~:/?#[\]@!$&\'()*+,;=%]*$'
          return re.match(https_pattern, surl)

     if True and ssl_check(link):
          flags += 1
          #print("-uses ssl protocol")
     else:
          pass
          #print("-does not use ssl protocol, not safe")

     def percentage_calculator(flags1,Total_checks):
          divides = (flags1/Total_Checks)
          percentage = int(divides*100)
          #print(f'Overall report % : {percentage}')
          return percentage
     report = percentage_calculator(flags,Total_Checks)

     return report

