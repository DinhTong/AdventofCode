import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl = http.request(
    'GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay11Input.txt')

# read the data from the URL and print it
rawData = webUrl.data.splitlines()

# rawData = ['L.LL.LL.LL',
#         'LLLLLLL.LL',
#         'L.L.L..L..',
#         'LLLL.LL.LL',
#         'L.LL.LL.LL',
#         'L.LLLLL.LL',
#         '..L.L.....',
#         'LLLLLLLLLL',
#         'L.LLLLLL.L',
#         'L.LLLLL.LL']

i = 0
# Identify matrix size
columns = len(rawData[i])
column = 1
rows = len(rawData)
row = 1
# Identify surrounding value. Default value = floor
tF = '.'  # top left
tT = '.'  # top
tR = '.'  # top right
rR = '.'  # right
bR = '.'  # bottom right
bB = '.'  # bottom
bL = '.'  # bottom left
lL = '.'  # left
# create floor
borderFloor = ''.join([char*columns for char in lL])
# Sub functions
minus = lambda x: x - 1
plus = lambda x: x + 1

#Day 11 part 1:
result1 = 0
counter = 1
# list of seats that change value
seatUpdate = rawData

while counter > 0:
    cleanData = []
    counter = 0
    # add top and bottom borders
    seatUpdate = [borderFloor] + seatUpdate + [borderFloor]
    # add left and right borders
    for i in seatUpdate:
        i = '.' + i + '.'
        cleanData.append(i)
    #Gather list of possible change seat value
    row = 1
    tempList = []
    while row <= rows:
        column = 1
        tempCol = ''
        while column <= columns:
            adjacent = []
            #Get surrounding value
            tF = cleanData[minus(row)][minus(column)]  # top left
            tT = cleanData[minus(row)][column]  # top
            tR = cleanData[minus(row)][plus(column)]  # top right
            rR = cleanData[row][plus(column)]  # right
            bR = cleanData[plus(row)][plus(column)]  # bottom right
            bB = cleanData[plus(row)][column]  # bottom
            bL = cleanData[plus(row)][minus(column)] # bottom left
            lL = cleanData[row][minus(column)]  # left
            #Add surrounding into adjacent list
            adjacent = [tF, tT, tR, rR, bR, bB, bL, lL]
            if cleanData[row][column] == 'L' and adjacent.count('#') == 0:
                tempCol = tempCol + '#'
                counter += 1
            elif cleanData[row][column] == '#' and adjacent.count('#') >= 4:
                tempCol = tempCol + 'L'
                counter += 1
            else:
                tempCol = tempCol + cleanData[row][column]
            column += 1
        tempList.append(tempCol)
        row += 1
    seatUpdate = []
    seatUpdate = tempList
#Count occupied seats
for i in seatUpdate:
    column = 0
    while column < columns:
        if i[column] == '#':
            result1 += 1
        column += 1

print ('Day 11 part 1 result : ' + str(result1))



