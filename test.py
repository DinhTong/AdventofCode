from collections import OrderedDict
from collections import Counter

#x = input('Enter test number : ')
x = "eao\nwoa\nao\noa"

# dataInput = x.replace("\n", "")

def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

#Count number of people in group
result1 = 0
pCount = Counter(x)
count = pCount['\n'] + 1
allAns = x.replace("\n","")
cCount = Counter(allAns)
simAns = removeDupWithOrder(allAns)

for i in simAns:
    chk = cCount[i]
    if chk == count:
        result1 = result1 + 1

#Count questions that everyone answered "yes"
#Count how many times a character appear in a string
def countQuestionEveryoneAnsweredYes (str):
    r = 0
    pCount = Counter(x) 
    count = pCount['\n'] + 1 #Count how many people in the group
    allAns = x.replace("\n","") #Combine all answers into one string
    cCount = Counter(allAns) #Function to count duplicate
    simAns = removeDupWithOrder(allAns) 
    for i in simAns:
        chk = cCount[i]
        if chk == count:
            r = r + 1
    return r

result = countQuestionEveryoneAnsweredYes(x)

print (result1)


