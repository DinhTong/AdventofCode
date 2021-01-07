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

# this is a better way to do the 2 way convert. I can expanse the crosswalk.
crossWalk = ['E-1','N-2','W-3','S-4']
# d2v = direction to value. This translates direction initial to value.
# v2d = value to direction. This translates value to direction initial.

def directionTranslator (x, y):
    for i in crossWalk:
        temp = i.split('-')
        val1 = temp[0]
        val2 = temp[1]
        if x == 'd2v' and y == val1:
            return val2
        elif x == 'v2d' and str(y) == val2:
            return val1

#Turn direction are either left (L) or right (R)
#Current direction must be first initial
#Turn degree can only be devisible by 90 (90, 180, 270, 360...)
def directionChanging (turnDirection, currentDirection, turnDegree):
    if turnDirection == 'L':
        currentDirection = int(directionTranslator('d2v',currentDirection)) #translate current direction to direction value
        currentDirection = left (currentDirection, turnDegree) #Calculate new direction using giving information
        currentDirection = directionTranslator('v2d',currentDirection) #translate new direction value to new direction initial
        return currentDirection
    elif turnDirection == 'R':
        currentDirection = int(directionTranslator('d2v',currentDirection)) #translate current direction to direction value
        currentDirection = right (currentDirection, turnDegree) #Calculate new direction using giving information
        currentDirection = directionTranslator('v2d',currentDirection) #translate new direction value to new direction initial
        return currentDirection

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
    elif aInstr(i) == 'L' or aInstr(i) == 'R':
        curDir = directionChanging(aInstr(i), curDir, int(aValue(i)))

result1 = abs(north) + abs(east)

print ('Day 12 part 1 result : ' + str(result1))

# Day 12 part 2
result2 = 0
waypoint = 'E-10-N-1'#Starting waypoint values: 10 units east and 1 unit north
shiplocation = 'E-0-N-0' 
curDir = 'E' #Current facing direction. Starting direction is East

for i in rawData:
    temp = waypoint.split('-')
    wp1 = temp[0]
    wp2 = int(temp[1])
    wp3 = temp[2]
    wp4 = int(temp[3])
    temp = shiplocation.split('-')
    sl1 = temp[0]
    sl2 = int(temp[1])
    sl3 = temp[2]
    sl4 = int(temp[3]) 
    action = aInstr(i)
    actionValue = int(aValue(i))

    if action == 'L' or action == 'R':
        wp1 = directionChanging(action, wp1, actionValue)
        wp3 = directionChanging(action, wp3, actionValue)
    #Ship first coordinate can only change from east to west and vice versa.
    #if waypoint FIRST coordinate store East and West value. Then match waypoint FIRST coordinate value to ship FIRST coordinate value.
    elif action == 'F' and (wp1 == 'E' or directionChanging('L', wp1, 180) == 'E'): 
        if wp1 == sl1 and wp3 == sl3:
            sl2 = sl2 + (wp2 * actionValue)
            sl4 = sl4 + (wp4 * actionValue)
        elif wp1 == directionChanging('L', sl1, 180) and wp3 == sl3:
            sl2 = sl2 - (wp2 * actionValue)
            sl4 = sl4 + (wp4 * actionValue)
        elif wp1 == sl1 and wp3 == directionChanging('L', sl3, 180):
            sl2 = sl2 + (wp2 * actionValue)
            sl4 = sl4 - (wp4 * actionValue)
        elif wp1 == directionChanging('L', sl1, 180) and wp3 == directionChanging('L', sl3, 180):
            sl2 = sl2 - (wp2 * actionValue)
            sl4 = sl4 - (wp4 * actionValue)
    #if waypoint FIRST coordinate does not store East and West value. Then match waypoint FIRST coordinate value to ship SECOND coordinate value
    elif action == 'F' and (wp1 != 'E' or directionChanging('L', wp1, 180) != 'E'): 
        if wp1 == sl3 and wp3 == sl1:
            sl2 = sl2 + (wp4 * actionValue)
            sl4 = sl4 + (wp2 * actionValue)
        elif wp1 == directionChanging('L', sl3, 180) and wp3 == sl1:
            sl2 = sl2 + (wp4 * actionValue)
            sl4 = sl4 - (wp2 * actionValue)
        elif wp1 == sl3 and wp3 == directionChanging('L', sl1, 180):
            sl2 = sl2 - (wp4 * actionValue)
            sl4 = sl4 + (wp2 * actionValue)
        elif wp1 == directionChanging('L', sl3, 180) and wp3 == directionChanging('L', sl1, 180):
            sl2 = sl2 - (wp4 * actionValue)
            sl4 = sl4 - (wp2 * actionValue)
    elif action == wp1:
        wp2 = wp2 + actionValue
    elif directionChanging('L', action, 180) == wp1:
        wp2 = wp2 - actionValue
    elif action == wp3:
        wp4 = wp4 + actionValue
    elif directionChanging('L', action, 180) == wp3:
        wp4 = wp4 - actionValue


    #Updating waypoint
    if wp2 < 0: #If value < 0 then switch to oppsite direction
        wp1 = directionChanging('L', wp1, 180)
        wp2 = wp2 * -1
    
    if wp4 < 0:
        wp3 = directionChanging('L', wp3, 180)
        wp4 = wp4 * -1
    waypoint = wp1 + '-' + str(wp2) + '-' + wp3 + '-' + str(wp4)
    #print ('Waypoint : ' + waypoint)

    #Updating ship location
    if sl2 < 0:
        sl1 = directionChanging('L', sl1, 180)
        sl2 = sl2 * -1

    if sl4 < 0:
        sl3 = directionChanging('L', sl3, 180)
        sl4 = sl4 * -1
    shiplocation = sl1 + '-' + str(sl2) + '-' + sl3 + '-' + str(sl4)
    #print ('Ship location : ' + shiplocation)


temp = shiplocation.split('-')
sl1 = temp[0]
sl2 = int(temp[1])
sl3 = temp[2]
sl4 = int(temp[3]) 

result2 = sl2 + sl4
print ('Day 12 part 2 result : ' + str(result2))

