import bs4
import requests

# GRABBING IMG TAGS FROM URL AND DISPLAYING THEIR IMAGE

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')
computer = soup.select('img')[0]

# Returns img source
print(computer['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# print(image_link.content)

# WB tag means writing to binary since image_link.content contains binary text
f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()
