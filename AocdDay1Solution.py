#
# read the data from the URL and print it
#
import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay1Input.txt')

#get the result code and print it
#print ("result code: " + str(webUrl.status))

# read the data from the URL and print it
data = webUrl.data
numList = data.splitlines()

#Begin For Loop
r = 0

for i in numList[r:]:
    r = r + 1
    for j in numList[r:]:
        if int(i) + int(j) == 2020:
            result = {
                "num1": i,
                "num2": j,
                "product": int(i) * int(j)
            }
            print result

#Begin For Loop - extra Star solution
lv1 = 0
lv2 = 1
lv3 = 2

for i in numList[lv1:]:
    for j in numList[lv2:]:
        for k in numList[lv3:]:
            if int(i) + int(j) + int(k) == 2020:
                result = {
                    "num1": i,
                    "num2": j,
                    "num3": k,
                    "product": int(i) * int(j) * int(k)
                }
                print result
        lv3 = lv3 + 1       
    lv1 = lv1 + 1
    lv2 = lv1 + 1
    lv3 = lv2 + 1 

