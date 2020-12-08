import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay3Input.txt')

# read the data from the URL and print it
data = webUrl.data.splitlines()

# print len(data[0])

#Day 3 part 1
#Begin for loop
posCalulation = lambda x, y : x + 3 - y if x + 3 > y else x + 3 #Calculate right 3 down 1
pos = 1
result1 = 0

for i in data:
    pos = pos - 1
    lenData = len(i)
    if i[pos] == '#':
        result1 = result1 + 1
    pos = posCalulation (pos + 1, lenData)

print ("Day 3 part 1 result : " ,result1)

#Day 3 part 2
#Begin for loop
r1d1 = lambda x, y : x + 1 - y if x + 1 > y else x + 1 #Right 1 down 1
r3d1 = lambda x, y : x + 3 - y if x + 3 > y else x + 3 #Right 3 down 1
r5d1 = lambda x, y : x + 5 - y if x + 5 > y else x + 5 #Right 5 down 1
r7d1 = lambda x, y : x + 7 - y if x + 7 > y else x + 7 #Right 1 down 1
ps11 = ps31 = ps51 = ps71 = ps12 = 1 #Character position for each scenarios
r1d1c = r3d1c = r5d1c = r7d1c = r1d2c = 0 #Tree count for each scenarios
result2 = 0

#Down 1
for i in data:
    lenData = len(i)
    ps11 = ps11 - 1
    ps31 = ps31 - 1
    ps51 = ps51 - 1
    ps71 = ps71 - 1
    #Right 1
    if i[ps11] == "#":
        r1d1c = r1d1c + 1
    ps11 = r1d1 (ps11 + 1, lenData)

    #Right 3
    if i[ps31] == "#":
        r3d1c = r3d1c + 1
    ps31 = r3d1 (ps31 + 1, lenData)

    #Right 5
    if i[ps51] == "#":
        r5d1c = r5d1c + 1
    ps51 = r5d1 (ps51 + 1, lenData)

    #Right 7
    if i[ps71] == "#":
        r7d1c = r7d1c + 1
    ps71 = r7d1 (ps71 + 1, lenData)

#Down 2
loop = 0 #loop count
ps12 = ps12 - 1
for j in data:
    loop = loop + 1
    lenData = len(j)
    if (loop % 2) == 0:
        continue
    else:
        if j[ps12] == "#":
            r1d2c = r1d2c + 1
        ps12 = r1d1 (ps12 + 1, lenData)
        ps12 = ps12 - 1
        #print j, " - Position : ", ps12-1 , " - Character : ", j[ps12-1] , " - Tree Count :", r1d2c , "Loop : ", loop
    

result2 = r1d1c * r3d1c * r5d1c * r7d1c * r1d2c
print ("Day 3 part 2 result : " ,result2)