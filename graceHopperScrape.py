import bs4
import requests

# GRABBING TABLE OF CONTENTS TAGS AND DISPLAYING THEIR TEXT

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')

# print(soup)
toc_text = soup.select('.toctext')
# print(toc_text)
for texts in toc_text:
    print(texts.text)
