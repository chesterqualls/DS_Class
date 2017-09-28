import re
sample = open("regex_sum_42.txt")

integers = list()
text = ""

for line in sample:
	text = text + " " + line.rstrip()
	integers = re.findall("[0-9]+", text)
    # integers.append(num)
	# return integers

# print integers

integers = map(int, integers)
answer = sum(integers)

print answer