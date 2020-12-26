import requests
import bs4

# BASIC BS4 CALLS TO SCRAPE DATA

result = requests.get("http://www.example.com")
# print(result.text)

soup = bs4.BeautifulSoup(result.text, 'lxml')
# print(soup)

print(soup.select('title')[0].getText())
site_paragraphs = soup.select('p')[0]
print(site_paragraphs)
print(site_paragraphs.getText())
