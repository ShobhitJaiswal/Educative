## importing bs4, requests and fake_useragent modules
import bs4
import requests
from fake_useragent import UserAgent
import csv

## initializing the UserAgent object
user_agent = UserAgent()
url = "https://www.consumerreports.org/cro/a-to-z-index/products/index.htm"

## getting the reponse from the page using get method of requests module
page = requests.get(url, headers={"user-agent": user_agent.chrome})

## storing the content of the page in a variable
html = page.content

## creating BeautifulSoup object
soup = bs4.BeautifulSoup(html, "html.parser")

## div tags with crux-body-copy class
div_class = "crux-body-copy"

## getting all the divs with class 'crux-body-copy'
div_tags = soup.find_all("div", class_=div_class)

## we will see all the div tags 
## enclosing the anchor tags with the required info
# for tag in div_tags:
#     print(tag)

## then we open a csv file in append mode
with open("product_data.csv", "a") as csv_file:
    writer = csv.writer(csv_file)

    ## extracting the names and links from the div tags
    for tag in div_tags:
        name = tag.a.text.strip()
        link = tag.a['href']
        
        # print("{} ---- {}".format(name, link))
        writer.writerow([name,link])