import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay5Input.txt')

# read the data from the URL and print it
data = webUrl.data.splitlines()

#print data[:3]

#Day 5 part 1
#Scanning seat 
result1 = 0
scanSeat = [] #Create an empty list to store scan result
alpha = lambda x, y: 0 if y - 1 == x else (y - x - 1) / 2 
# upperM = lambda x, y: y if y - 1 = x else (y - x + 1) / 2 #lower limit of the upper group 
# lowerM = lambda x, y: x if y - 1 = x else (y - x - 1) / 2 #upper limit of the lower group

for i in data:
    if len(i) == 0:
        continue
    else:
        dataLen = len(i) - 1 #Python index Zero in String position
        charPos = 0
        ulRow = 127 #Upper limit Row
        llRow = 0 #Lower limit Row
        ulCol = 7 #Upper limit Column
        llCol = 0 #Lower limit Column
        row = 0
        seat = 0
        for j in i:
            if charPos < 6:
                if j == "B":
                    llRow = ulRow - alpha (llRow, ulRow) 
                elif j == "F":
                    ulRow = llRow + alpha (llRow, ulRow)
            elif charPos == 6:
                if j == "B":
                    row = ulRow
                elif j == "F":
                    row = llRow
            elif 6 < charPos < dataLen:
                if j == "R":
                    llCol = ulCol - alpha (llCol, ulCol)
                elif j == "L":
                    ulCol = llCol + alpha (llCol, ulCol)
            elif charPos == dataLen:
                if j == "R":
                    seat = ulCol
                elif j == "L":
                    seat = llCol
            charPos = charPos + 1
    #scanSeat.append ("Row : "+ str(row) +" - Seat : "+ str(seat) +" - ID : "+ str(row * 8 + seat) +" - "+ i)
    scanSeat.append (row * 8 + seat)
print "Day 5 part 1 result: ", max(scanSeat)

#Day 5 part 2
#Finding seat
result2 = 0
scanSeat.sort()
mPoint = len(scanSeat)
for k in scanSeat[1:mPoint]:
    if k + 1 not in scanSeat:
        result2 = k + 1
        break

print "Day 5 part 2 result: ", result2
              