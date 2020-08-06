#######
#otsoy#
#######

text = open("/Users/otsoy/Desktop/otsoy/python/numb.txt", "r") #directory of file
data = list(text.read())
line = len(data)

print ("unsort", data)

for i in range(line):
	for j in range(line-1):
		if data[j] > data[j+1]:
			data[j], data[j+1] = data[j+1],data[j]
print("sort", data)
text.close