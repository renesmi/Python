text = open('text2.txt','r')
//count = 0

while True:
	//count += 1
	line = text.readline()
	search ="살것"
	if not line: break
	if line.find(search) != -1 :
		output = line


text.close()
