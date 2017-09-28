import urllib
import xml.etree.ElementTree as ET

url=raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
lst = tree.findall('.//count')
print 'Count:', len(lst)
total = 0
for comment in tree.findall("./comments/comment"):
    total += int(comment.find('count').text)
print "Sum: ", total