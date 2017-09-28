import urllib
from BeautifulSoup import *
taglist=list()
url=raw_input("Enter URL: ")
count=int(raw_input("Enter count:"))
position=int(raw_input("Enter position:"))
for i in range(count):
    print "Retrieving:",url
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    for tag in tags:
        taglist.append(tag)
    url = taglist[position-1].get('href', None)
    del taglist[:]
print "Retrieving:",url