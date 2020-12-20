import urllib3
from collections import OrderedDict
from collections import Counter

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay6Input.txt')

# read the data from the URL and print it
data = webUrl.data.split("\n\n")

#Remove duplicate characters within a string
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

#Count questions that everyone answered "yes"
#Count how many times a character appear in a string
def countQuestionEveryoneAnsweredYes (str):
    r = 0
    pCount = Counter(str) 
    count = pCount['\n'] + 1 #Count how many people in the group
    allAns = str.replace("\n","") #Combine all answers into one string
    cCount = Counter(allAns) #Function to count duplicate
    simAns = removeDupWithOrder(allAns) 
    for i in simAns:
        chk = cCount[i]
        if chk == count:
            r = r + 1
    return r

#Day 6 part 1
#Remove duplicate chars within a string
result1 = 0
for i in data:
    i = i.replace("\n","")
    result1 = result1 + len(removeDupWithOrder(i))
print ("Day 6 part 1 result: ", result1)

#Day 6 part 2
result2 = []
for i in data:
    r = countQuestionEveryoneAnsweredYes(i)
    result2.append(r)

print ("Day 6 part 2 result: ", sum(result2))


