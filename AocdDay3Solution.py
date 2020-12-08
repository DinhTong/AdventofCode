import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay3Input.txt')

# read the data from the URL and print it
data = webUrl.data.splitlines()

# print len(data[0])


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

print result1



