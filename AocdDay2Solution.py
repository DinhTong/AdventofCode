import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay2Input.txt')

# read the data from the URL and print it
data = webUrl.data.splitlines()


#Day2 part 1
#Begin For Loop
resultDay1 = 0

for string in data:

    #Parsing string
    llim = string.split("-")[0]
    tempStr = string.split("-")[1]
    ulim = tempStr.split(" ")[0]
    p = tempStr.split(" ")[1].replace(":","")
    pwChk = tempStr.split(" ")[2].count(p) 

    #Check for valid password
    if int(llim) <= int(pwChk) <= int(ulim):
        resultDay1 = resultDay1 + 1

print resultDay1


#Day2 part 2
#Begin For Loop
resultDay2 = 0

for string in data:

    #Parsing string
    llim = int(string.split("-")[0]) - 1 #To handle index zero
    tempStr = string.split("-")[1]
    ulim = int(tempStr.split(" ")[0]) - 1 #To handle index zero
    p = tempStr.split(" ")[1].replace(":","")
    pwStr = tempStr.split(" ")[2]

    #Check for valid password
    if pwStr[llim] == p != pwStr[ulim] or pwStr[llim] != p == pwStr[ulim]:
        resultDay2 = resultDay2 + 1

print resultDay2

