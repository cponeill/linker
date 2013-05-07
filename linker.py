# The comments are just for my own educational purposes. This code snippet is actually pretty easy to read and understand.

from bs4 import BeautifulSoup
from urllib2 import urlopen

# This is the code that accesses the URL and reads the contents on the web page. 
url = urlopen(raw_input("Enter a web address here: "))
content = url.read()
url.close()

# Here is where assign the variable "content" to "soup" and find all the letter "a" in the code base of the webpage. From there
# I assign it to "linker" in the loop and print out all the "href" links to read.
soup = BeautifulSoup(content)
find = soup.find_all("a")
for linker in soup.find_all('a'):
    print (linker.get("href"))
