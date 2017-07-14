import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')
uh = urllib.urlopen(serviceurl)
data = uh.read()
#print data
    
cmment = ET.fromstring(data)
lst = cmment.findall('comments/comment')
#print len(lst)
#print lst

i = int(0)
num2 = int(0)

for item in lst:
    #print item.find('name').text
    i = i + 1
    num = int(item.find('count').text)
    #suma2 = suma[int(i)] + suma[int(i+1)] 
    #print num
    
    num2 = num2 + num

print 'Retrieving', serviceurl 
print 'Retrieved',len(data),'characters'   
print 'Count', i 
print 'Sum:', num2

#http://python-data.dr-chuck.net/comments_255894.xml
