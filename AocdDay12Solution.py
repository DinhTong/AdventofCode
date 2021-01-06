import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl = http.request(
    'GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay12Input.txt')

# read the data from the URL and print it
rawData = webUrl.data.splitlines()

# rawData = ['F10',
# 'N3',
# 'F7',
# 'R90',
# 'F11']

#print rawData

# All turn degrees are devisible by 90 
# East = 1 ; North = 2 ; West = 3 ; South = 4
left = lambda  currentDirection, turnDegree: currentDirection + (turnDegree/90) if (currentDirection + (turnDegree/90)) <= 4 else (currentDirection + (turnDegree/90)) - 4
right = lambda currentDirection, turnDegree: currentDirection - (turnDegree/90) if (currentDirection - (turnDegree/90)) > 0 else (currentDirection - (turnDegree/90)) + 4
aInstr = lambda string: string[0]
aValue = lambda string: string[1:len(string)]

# want to find a better way to build this 2 way dict (Oldway)
def dirConvert (val):
    if val == 1:
        return 'E'
    elif val == 2:
        return 'N'
    elif val == 3:
        return 'W'
    elif val == 4:
        return 'S'
    elif val == 'E':
        return 1
    elif val == 'N':
        return 2
    elif val == 'W':
        return 3
    elif val == 'S':
        return 4

# this is a better way to do the 2 way convert. I can expanse the crosswalk.
crossWalk = ['E-1','N-2','W-3','S-4']
# d2v = direction to value. This translates direction initial to value.
# v2d = value to direction. This translates value to direction initial.
def directionTranslator (x, y):
    if x == 'd2v':
        for i in crossWalk:
            temp = i.split('-')
            val1 = temp[0]
            val2 = temp[1]
            if y == val1:
                return val2
                break
    elif x == 'v2d':
        for i in crossWalk:
            temp = i.split('-')
            val1 = temp[0]
            val2 = temp[1]
            if str(y) == val2:
                return val1
                break


curDir = 'E' #Current facing direction. Starting direction is East
north = 0 #Starting position North - 0, negative north value = positive south value
east = 0 #Starting position East - 0, negative east value = positive west value


# Day 12 part 1

for i in rawData:
    if aInstr(i) == 'N' or (aInstr(i) == 'F' and curDir == 'N'):
        north = north + int(aValue(i))
    elif aInstr(i) == 'S' or (aInstr(i) == 'F' and curDir == 'S'):
        north = north - int(aValue(i))
    elif aInstr(i) == 'E'or (aInstr(i) == 'F' and curDir == 'E'):
        east = east + int(aValue(i))
    elif aInstr(i) == 'W'or (aInstr(i) == 'F' and curDir == 'W'):
        east = east - int(aValue(i))
    elif aInstr(i) == 'L':
        curDir = int(directionTranslator('d2v',curDir)) #translate current direction to direction value
        curDir = left (curDir, int( aValue(i))) #Calculate new direction using giving information
        curDir = directionTranslator('v2d',curDir) #translate new direction value to new direction initial
    elif aInstr(i) == 'R':
        curDir = int(directionTranslator('d2v',curDir)) #translate current direction to direction value
        curDir = right (curDir, int( aValue(i))) #Calculate new direction using giving information
        curDir = directionTranslator('v2d',curDir) #translate new direction value to new direction initial
        
        
        #curDir = directionTranslator('v2d',right (directionTranslator('d2v',curDir),int(aValue(i))))


result1 = abs(north) + abs(east)

print 'Day 12 part 1 result : ' + str(result1)