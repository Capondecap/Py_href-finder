import urllib.request
from bs4 import BeautifulSoup
import ssl



inp = input('Enter your link: ')
context = ssl._create_unverified_context()

url =  urllib.request.urlopen(inp, context=context).read()
soup = BeautifulSoup(url,'html.parser')
anchor = soup("a")
for i in anchor:
    print(i.get("href"))

