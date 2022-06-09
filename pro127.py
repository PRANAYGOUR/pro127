from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests 

BrightStar_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(BrightStar_URL)
soup = bs(page.text , "html.parser")
star_table = soup.find("table")

temp_list = []

tableRows = star_table.find_all("tr")
for tr in tableRows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]

    temp_list.append(row)

star_name = []
star_distance = []
star_radius = []
star_lum = []
star_mass = []

for i in range(1 , len(temp_list)):
    star_name.append(temp_list[i][1])
    star_distance.append(temp_list[i][3])
    star_mass.append(temp_list[i][5])
    star_radius.append(temp_list[i][6])
    star_lum.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(star_name,star_distance,star_mass,star_radius,star_lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv("BrightStar.csv")