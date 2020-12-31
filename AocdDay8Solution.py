import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay8Input.txt')

# read the data from the URL and print it
data = webUrl.data.splitlines()

#print data

# get added value
def signal(s):
    return s[:1]
# get operations
def ops(s):
    return s[:3]
# get signs
def sig(s):
    return s[4:5]
# get values
def val(s):
    return s[5:]

#Day 8 part 1
result1 = 0
visitedList = [] #To store a list of visited instructions
upperLim = len(data)
i = 0

while 0 <= i < upperLim:
    if i in visitedList:
        break
    else:
        visitedList.append(i)
        #print ("Position : ",str(i), " -- Accumulator : ", str(result1))
        if ops(data[i]) == 'nop':
            i += 1   
            #continue
        elif ops(data[i]) == 'jmp':
            if sig(data[i]) == '+':
                i = i + int(val(data[i]))
            else:
                i = i - int(val(data[i]))
            #continue
        elif ops(data[i]) == 'acc':
            if sig(data[i]) == '+':
                result1 = result1 + int(val(data[i]))
            else:
                result1 = result1 - int(val(data[i]))
            i += 1

print ("Day 8 part 1 result: ", result1)

#Day 8 part 2
result2 = 0
visitedList = [] #To store a list of visited instructions
upperLim = len(data) - 1
i = 0

while 0 <= i <= upperLim:
    inst = ops(data[i])
    sign = sig(data[i])
    value = int(val(data[i]))
    print ("Raw : " , data[i], " - Parsed : ", inst , " | ", sign , " | ", str(value))
    if inst == 'nop':
        if (i + value) == upperLim and sign == '+':
            i = i + value
        else:
            i += 1
    elif inst == 'jmp':
        if  i + 1 == upperLim:
            i += 1
        elif sign == '+':
            i = i + value
        else:
            i = i - value
    elif inst == 'acc':
        if sign == '+':
            result2 = result2 + value
        else:
            result2 = result2 - value
        i += 1


print ("Day 8 part 2 result: ", result2)