import re
Ch11Txt = open("regex_sum_286995.txt")

integers = list()
text = ""

for line in Ch11Txt:
	text = text + " " + line.rstrip()
	integers = re.findall("[0-9]+", text)
    
integers = map(int, integers)
Ch11Sum = sum(integers)

print Ch11Sum