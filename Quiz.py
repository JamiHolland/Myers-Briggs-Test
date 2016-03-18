from NSQuestions import NSQuestions
print NSQuestions

result = {
	"N":0,
	"S":0, 
	"I":0, 
	"E":0, 
	"F":0, 
	"T":0, 
	"J":0, 
	"P":0
}

for Question in NSQuestions:
	print 1, Question["N"]
	print 2, Question["S"]
	userinput = raw_input("Please input 1 or 2 for your choice.")
	if userinput == "1":
		result["N"]+=1
	elif userinput == "2":
		result["S"]+=1



#end
print "you are an ", "N" if result["N"]>result["I"] else "S"