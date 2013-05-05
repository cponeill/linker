from bs4 import BeautifulSoup
from urllib2 import urlopen

url = urlopen(raw_input("Enter a web address here: "))
content = url.read()
url.close()

soup = BeautifulSoup(content)
find = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get("href"))
