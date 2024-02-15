from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
import time 
import pandas as pd

start_url = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/lerod/Desktop/BIJUS Daniel/aula 127/chrome-win64/chrome.exe")
browser.get(start_url)
time.sleep(2)
planet_data = []
def scrap():
    for i in range(0,10):
        print(f"coletando dados")
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs = {"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else: 
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
        planet_data.append(temp_list)
    browser.find_element(by=By.XPATH,value="//*[@id='primary_column']/footer/div/div/div/nav/span[2]/a").click()
scrap()

