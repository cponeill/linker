from bs4 import BeautifulSoup
from urllib2 import urlopen

url = urlopen(raw_input("Enter a web address here: "))
content = url.read()
url.close()

soup = BeautifulSoup(content)
find = soup.find_all("a")
for linker in soup.find_all('a'):
    print (linker.get("href"))
