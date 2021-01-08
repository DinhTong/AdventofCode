import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl = http.request(
    'GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay13Input.txt')

# read the data from the URL and print it
rawData = webUrl.data.splitlines()

print rawData