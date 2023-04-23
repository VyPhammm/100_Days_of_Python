from bs4 import BeautifulSoup
import requests

response= requests.get("https://news.ycombinator.com")
yc_webpage= response.text

soup= BeautifulSoup(yc_webpage, "html.parser")

articles= soup.find_all( "span", class_= "titleline")
article_tags= [tag.find("a") for tag in articles]

article_texts= []
article_links= []
for article_tag in article_tags:
        text= article_tag.getText()
        article_texts.append(text)
        link= article_tag.get("href")
        article_links.append(link)

article_upvotes= [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
index_max= article_upvotes.index(largest_number)
print(article_upvotes[index_max])
print(article_texts[index_max])
print(article_links[index_max])