#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

def frshodan(query, sleep_time):
    url = "https://www.shodan.io/search/facet?query=" + urllib.parse.quote(query) + "&facet=ip"
    response = requests.get(url)
    ip_list = []
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a", class_="text-dark")
        
        for link in links:
            strong_tag = link.find("strong")
            if strong_tag:
                ip_address = strong_tag.text.strip()
                ip_list.append(ip_address)
                time.sleep(sleep_time)
        return ip_list
    else:
        return "err: status_code: " + str(response.status_code)
