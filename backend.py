#Phishing Website Detector
#PWD Backend

import requests
import whois
from datetime import datetime

#getting url input

link=input("URL:")
linkdata = whois.whois(link)
print(linkdata)

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
     print("the domain creation date is older than a year")
else:
     print("the domain creation date is lesser than a year")