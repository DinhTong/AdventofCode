import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl = http.request(
    'GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay10Input.txt')

# read the data from the URL and print it
#data = webUrl.data.splitlines()

#data = [16,10,15,5,1,11,7,19,6,12,4]
data = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
#Add starting effective rating
data = [int(i) for i in data]
data.extend([0, max(data) + 3])
data = sorted(data)
print (data)

joltType = lambda x, y : y - x

# Day 10 part 1
result1 = 0
lenList = len(data)
i = 0
# count jolts
jolt1 = 0
jolts3 = 0

while i + 1 < lenList:
    if joltType(data[i],data[i+1]) == 1:
        jolt1 += 1
    elif joltType(data[i],data[i+1]) == 3:
        jolts3 += 1
    else:
        print ("Found unexpected condition!!")
        break
    i += 1

result1 = jolt1 * jolts3
print ('Day 10 part 1 result : ' + str(result1))

# Day 10 part 2
result2 = 1
i = 0
possible_Path = 0
possible_Combination = []

while i + 1 < lenList:
    x = data[i]
    n1 = data[i+1]
    if lenList == (i + 3):
        n3 = 0
        n2 = data[i+2]
    elif lenList == (i + 2):
        n3 = 0
        n2 = 0
    else:
        n3 = data[i+3]
        n2 = data[i+2]
    for j in range (1,4):
        if x + j == n1 or x + j == n2 or x + j == n3:
            possible_Path += 1
        j += 1
    possible_Combination.append(possible_Path)
    possible_Path = 0
    i += 1
#Remove zero from possible combination list
possible_Combination = [i for i in possible_Combination if i != 0 and i != 1]
print possible_Combination

# for i in possible_Combination:
result2 = result2 + sum(possible_Combination)

print ('Day 10 part 2 result : ' + str(result2))