from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import requests

url= 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
header= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
}

response= requests.get(url, headers= header)

soup= BeautifulSoup(response.text, "html.parser")

#TASK1: Get infomation: link, address, price

all_link_elements = soup.select("div.result-list-container ul li div div article a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    # print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address = soup.select("div.result-list-container ul li div div article a address")
address_list = [address.get_text().split('|')[-1] for address in all_address]

all_prices =  soup.select("div.result-list-container ul li div div article div span")
price_list = [price.get_text().split("+")[0] for price in all_prices if "$" in price.text]

print(all_links)
print(address_list)
print(price_list)

#TASK2: Fill info to google form

form_url= "https://forms.gle/rtfF6YTxNo6LqsVn8"
chrome_driver_path= r"D:/Development/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path) 
driver = webdriver.Chrome(options= options, service=service) 

for i in range(len(all_links - 1)):
    driver.get(form_url)
    sleep(5)
    address_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button= driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')    

    address_button.send_keys(address_list[i])
    sleep(2)

    price_button.send_keys(price_list[i])
    sleep(2)

    link_button.send_keys(all_links[i])
    sleep(2)

    submit_button.click()
    sleep(5)

 
print("Complete!!!")





