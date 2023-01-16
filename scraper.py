from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

#Website URL
URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(URL)

time.sleep(5)
stars_data =[]
star_list = []
#Define data scrapping method
def scrape():
    print('Scrapping page ....')
    

    soup = BeautifulSoup(browser.page_source,"html.parser")

    for table in soup.find_all("table",attrs={"class","wikitable sortable jquery-tablesorter"}):
        for tr_tags in table.find_all("tr"):
            td_tags = tr_tags.find_all("td")
            temp_list = []
            i = 0
            for index,td_tag in enumerate(td_tags):
                     #print(f"Tag : {index} : ", td_tag)
                     #time.sleep(2)
                     if index == 1 or index == 2:
                          try:
                            li_1 = td_tag.find_all("a")[0].contents[0]
                            temp_list.append(li_1)
                          except:
                            temp_list.append("")
                     elif index == 0 or index == 3:
                          try:
                            temp_list.append(td_tag.find_all("span")[0].contents[0])
                          except:
                            temp_list.append("")     
                     else:
                      try:
                        li_3 = td_tag.contents[0]
                        temp_list.append(li_3)

                      except:
                        temp_list.append("")
                     #time.sleep(2)
            star_list.append(temp_list)
            #print(star_list)
        

#Define headers
headers = ["V mag","Proper Name","Bayer designation","Distance(ly)","Spectral class","Mass","Radius","Luminosity"]

#Call function to Scrape
scrape()

#Define pandas DataFrame
data_frame = pd.DataFrame(star_list,columns=headers)
data_frame.to_csv('data.csv',index=True,index_label=id)
#print(len(star_list))


        

