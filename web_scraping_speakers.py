# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import  requests
from bs4 import BeautifulSoup
import datetime
import csv

url = "https://www.salesforce.com/dreamforce/speakers/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36", "Connection": "close"}

#checking response from server == 200
page_response = requests.get(url, headers=headers) 
raw_html = page_response.content

#parse the html code
soup = BeautifulSoup(raw_html, "html.parser")

person_containers = soup.find_all("div", {"class": "face"})

#create the data block for each person ex.(name, title, company, image_url)
with open('salesforce_speaker.csv', 'w') as csvfile:
    person_writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for person in person_containers:
        name = person.h3.get_text()
        title_company = person.h4.get_text()
        image_url = "https:" + person.img['src']
        date_scraped = datetime.datetime.now()
        
        print("="*10)
        print(name)
        print(title_company)
        print(image_url)
        print(date_scraped)
        person_writer.writerow([name, title_company, image_url, date_scraped])
            

    
