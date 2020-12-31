import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay8Input.txt')

# read the data from the URL and print it
data = webUrl.data.splitlines()

#print data



for i in data:
    if 