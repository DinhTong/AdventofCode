import urllib3
from collections import OrderedDict

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay6Input.txt')

# read the data from the URL and print it
data = webUrl.data.split("\n\n")

#Day 6 part 1
#Remove duplicate chars within a string
result1 = 0
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

for i in data:
    i = i.replace("\n","")
    result1 = result1 + len(removeDupWithOrder(i))

print result1
