from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path= r"D:/Development/chromedriver.exe"
driver= webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("https://www.python.org/")

time_latest_news= driver.find_elements(By.CSS_SELECTOR, 'div.list-widgets.row > div.medium-widget.blog-widget > div > ul > li > time')
title_latest_news= driver.find_elements(By.CSS_SELECTOR, 'div.list-widgets.row > div.medium-widget.blog-widget > div > ul > li > a')
latest_news= {}
for n in range(len(time_latest_news)):
    latest_news[n]={
        "time":time_latest_news[n].text,
        "title":title_latest_news[n].text,
    }

print(latest_news)
    
