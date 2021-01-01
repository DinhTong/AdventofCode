import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl = http.request(
    'GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay9Input.txt')

# read the data from the URL and print it
data = webUrl.data.splitlines()


#data = ['35','20','15','25','47','40','62','55','65','95','102','117','150','182','127','219','299','277','309','576']
# print data

# day 9 part 1
result1 = 0
itemPos = len(data) - 1
startPoint = 0
endPoint = 0
counter = 0
loop = 1
# set distance
preAmbDis = 25
i = preAmbDis

while i <= itemPos:
    result1 = int(data[i])
    startPoint = i - preAmbDis
    endPoint = i
    for j in data[startPoint:endPoint]:
        #print ('This is j number : ' + j)
        for q in data[startPoint + loop:endPoint]:
            #print ('This is q number : ' + q)
            if int(j) + int(q) == result1:
                counter += 1
                #print ('This is counter : ' + str(counter))
        loop += 1

    if counter == 0:
        break
    else:
        i += 1
        counter = 0
        loop = 1

print('Day 9 part 1 result : ' + str(result1))

# day 9 part 2
result2 = 0
i = 0
loop = len(data)
counter = 0
#convert string list to int list
data = [int(i) for i in data]


while loop > 0 and counter == 0:
    while int(i) + int(loop) <= len(data) and counter == 0:
        print ('loop = ' + str(loop) + ' - i = ' + str(i) + ' SUM = ' + str(loop + i))
        sumList = sum(data[i:i+loop])
        maxList = max(data[i:i+loop])
        minList = min(data[i:i+loop])
        if sumList == result1:
            result2 = maxList + minList
            counter += 1
            break
        i += 1
    i = 0
    loop -= 1

print('Day 9 part 2 result : ' + str(result2))
