import requests
import bs4
# from fake_useragent import UserAgent

res=requests.get("https://www.wedmegood.com/vendors/all/wedding-photographers/")
# print(res.status_code)

soup=bs4.BeautifulSoup(res.content,'html.parser')
# print(soup.a["href"])

body=soup.body
contents=body.contents

# for tag in contents:
#     if tag != "\n":
#         print(tag, end="\n")
name_tags=soup.find_all("div",class_="frow")
city_tag=soup.find_all("div",class_="line")

# print(a_tags)
for name in name_tags:
    for city in city_tag:
        if name.a != None and city.span != None:
            print(name.a.text, city.span.text)    
            continue
    # else:
    #     pass
