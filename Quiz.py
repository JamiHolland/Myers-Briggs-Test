from NSQuestions import NSQuestions
#print NSQuestions
from FTQuestions import FTQuestions
#print FTQuestions
from IEQuestions import IEQuestions
#print IEQuestions
from JPQuestions import JPQuestions
#print JPQuestions
from MyersBriggsTypes import TYPES
# print	TYPES

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
def Quizzer (Questions, Type1, Type2, result):
	for Question in Questions:
		print 1, Question[Type1]
		print 2, Question[Type2]
		userinput = raw_input("Please input 1 or 2 for your choice.")
		if userinput == "1":
			result[Type1]+=1
		elif userinput == "2":
			result[Type2]+=1

Quizzer(NSQuestions,"N","S",result)
Quizzer(FTQuestions,"F","T",result)
Quizzer(IEQuestions,"I","E",result)
Quizzer(JPQuestions,"J","P",result)

#results 
# import pdb
# pdb.set_trace()
TestResults = ""
TestResults += "I" if result["I"]>result["E"] else "E"
TestResults += "N" if result["N"]>result["S"] else "S"
TestResults += "F" if result["F"]>result["T"] else "T"
TestResults += "J" if result["P"]>result["J"] else "P"

print "you are an ", TestResults

print "A", TestResults, "has the following qualities:", TYPES[1][TestResults]

# Ahmad is working here!