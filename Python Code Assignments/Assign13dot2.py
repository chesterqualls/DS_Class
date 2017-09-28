import json
import urllib
counts = list()
inp = raw_input('Enter a URL: ')
print "Retrieving:",inp

url = urllib.urlopen(inp)
data = url.read()

try:
    js = json.loads(data)
except:
    js = None

comments = js['comments']
for comment in comments:
    counts.append(comment['count'])
    
	
print "Retrieved ",len(data), "characters"
print "Count: ", len(counts)
print "Sum: ",sum(counts)
