from NSQuestions import NSQuestions
print NSQuestions
from FTQuestions import FTQuestions
print FTQuestions
from IEQuestions import IEQuestions
print IEQuestions
from JPQuestions import JPQuestions
print JPQuestions
from MyersBriggsTypes import MyersBriggsTypes
print	MyersBriggsTypes

from shuffle import shuffle
shuffle (NSQuestions)
shuffle (FTQuestions)
shuffle (IEQuestions)
shuffle (JPQuestions)


#while loop if user wants to continue the test?
#ask for user name?
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

#results 
print "you are an ", "N" if result["N"]>result["S"] else "S"



for Question in FTQuestions:
	print 1, Question["F"]
	print 2, Question["T"]
	userinput = raw_input("Please input 1 or 2 for your choice.")
	if userinput == "1":
		result["F"]+=1
	elif userinput == "2":
		result["T"]+=1

#results 
print "you are an ", "F" if result["F"]>result["T"] else "T"



for Question in IEQuestions:
	print 1, Question["I"]
	print 2, Question["E"]
	userinput = raw_input("Please input 1 or 2 for your choice.")
	if userinput == "1":
		result["I"]+=1
	elif userinput == "2":
		result["E"]+=1

#results 
print "you are an ", "I" if result["I"]>result["E"] else "E"



for Question in JPQuestions:
	print 1, Question["J"]
	print 2, Question["P"]
	userinput = raw_input("Please input 1 or 2 for your choice.")
	if userinput == "1":
		result["J"]+=1
	elif userinput == "2":
		result["P"]+=1


#results 
print "you are an ", "J" if result["P"]>result["J"] else "P"

# Ahmad is working here!