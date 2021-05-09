with open('sample.html') as file:
    html=file.read()

# from os import link
import bs4

soup=bs4.BeautifulSoup(html,"html.parser")

# print(soup.prettify())
link = soup.a
# print(link['href'])

body=soup.body

content=body.contents

print(type(content))
# for i in content:
#     print(i, end="\n")

for i in body.descendants:
    print(i, end="\n")
