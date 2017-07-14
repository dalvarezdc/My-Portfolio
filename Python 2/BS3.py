import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


i = 0
r = (raw_input('Enter count - '))
cl = int(raw_input('Enter position - '))
cl = cl - 1

print url
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    if int(i) < int(r):
        print tags[int(cl)].get('href', None) 
        url = tags[int(cl)].get('href', None)   
        i = i + 1
    
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
    else:    
        break
