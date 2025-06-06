import urllib.request
from bs4 import BeautifulSoup
import ssl

inp = input('Enter your link: ')

#ignore ssl cerificate (not recommended)
context = ssl._create_unverified_context()

#open read link
url =  urllib.request.urlopen(inp, context=context).read()

#parse data 
soup = BeautifulSoup(url,'html.parser')

#find href tag
anchor = soup("a")
for i in anchor:
    print(i.get("href"))

