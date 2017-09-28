name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

fh = open(name)

hours = dict()

for line in fh:
   if line.startswith("From "):

    hour = line.split()[5].split(':')[0] 
	
    hours[hour] = hours.get(hour, 0) + 1

for key, value in sorted(hours.items(), None):
    print key, value