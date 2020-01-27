#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 9 17:19:26 2018

@author: Jiarong Zhang; Mengxi Shen
"""

# -*- coding: utf-8 -*-
import csv,re,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
# Write Unsorted CSV File
with open("utags.csv", "w") as unsorted_file:
    writer = csv.writer(unsorted_file, delimiter=',')
# Go through the first 1,000 questions 
    page_number = 1
    if page_number in range(1,21):
        web_page = ["https://stackoverflow.com/questions/tagged/java?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/c?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/c++?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/python?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/c%23?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/vb.net?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/php?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/javascript?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/delphi?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/ruby?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/sql?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/vb6?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/r?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/plsql?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/assembly?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/swift?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/perl?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/go?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/matlab?page={}&sort=newest&pagesize=50",
                    "https://stackoverflow.com/questions/tagged/objective-c?page={}&sort=newest&pagesize=50"]
        for page in web_page:
            web_pages = page.format(page_number)
            with urlopen(web_pages) as url:
                soup = BeautifulSoup(url, "lxml")
# Extract questions
            for question in soup.find_all("div", class_="summary"):
                titles = question.h3.a.text
# Extract tags 
            tags = soup.find_all("div",class_="tags")
            all_tags_list = []
            for item in tags:
                tag = re.sub(r'\n', '',item.text).split()
                all_tags_list.extend(tag)
# Identify and Remove the seed tag
            seed_tags = Counter(all_tags_list).most_common(1)[0][0]
            sister_tags_list = [t for t in all_tags_list if t != seed_tags]
# Find the ten most frequently used sister tags aside from the seed tag itself
            fsister_tag = Counter(sister_tags_list).most_common(10)
            fsister_tags_list = [fsister_tag[i][0] for i in range(10)]
# Extract the total number of tagged questions
            if page_number == 1:
                total_number = re.sub(r'\D', '', (soup.find("div", class_="summarycount al")).text)
# Write content
            writer.writerow([seed_tags,total_number,fsister_tags_list[0],fsister_tags_list[1],fsister_tags_list[2],fsister_tags_list[3],fsister_tags_list[4],fsister_tags_list[5],fsister_tags_list[6],fsister_tags_list[7],fsister_tags_list[8],fsister_tags_list[9]])
# Cache folder for the downloaded pages        	
            def createaFolder(directory):
                try:
                   if not os.path.exists(directory):
                        os.makedirs(directory)
                except OSError:
                    print('Error: Creating directory. ' +  directory)

            createaFolder('NewFile')
            pnumber = int(re.sub(r'\D', '', (soup.find("span", class_="page-numbers current")).text))
            setag = re.sub(r'about', '',re.sub(r'\n', '',soup.find("div",class_="tagged").text))
            fi = open('NewFile/' + setag + "-%03d.html" % pnumber, 'wb')
            html = urlopen(web_pages).read()
            fi.write(html)
            fi.close()
        
        
        page_number += 1
       
# Sort the CSV file
content = csv.reader(open("utags.csv", "r"), delimiter = ",")
sorted_content = sorted(content, key=lambda row:int(row[1]), reverse = True)
with open("tags.csv", "w") as sorted_file:
    writer = csv.writer(sorted_file, delimiter = ",")
    writer.writerow(["Language", "Count", "Tag 1", "Tag 2", "Tag 3", "Tag 4", "Tag 5", "Tag 6", "Tag 7", "Tag 8", "Tag 9", "Tag 10"])
    for row in sorted_content:
        writer.writerow(row)

