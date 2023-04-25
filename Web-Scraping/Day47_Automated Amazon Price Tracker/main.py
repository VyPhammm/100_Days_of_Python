import requests
from bs4 import BeautifulSoup
import lxml

URL= "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
}

response= requests.get(URL, headers= header)

soup= BeautifulSoup(response.text, "lxml")
# print(soup.prettify())
price = soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay", data-a-color="base")
print(price)
