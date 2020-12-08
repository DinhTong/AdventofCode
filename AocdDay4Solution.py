import urllib3

# open a connection to a URL using urllib
http = urllib3.PoolManager()
webUrl  = http.request('GET', 'https://raw.githubusercontent.com/DinhTong/AdventofCode/main/AocdDay4Input.txt')

# read the data from the URL and print it
data = webUrl.data.split("\n\n")

#Day 4 part 1
#Validate valid passport
result1 = 0

for i in data:
    passport = i.replace("\n"," ")
    if "byr:" not in passport: #Check birth year field
        continue
    else:
        if "iyr:" not in passport: #Check issue year field
            continue
        else:
            if "eyr:" not in passport: #Check expiration year field
                continue
            else:
                if "hgt:" not in passport: #Check height field
                    continue
                else:
                    if "hcl:" not in passport: #Check hair color field
                        continue
                    else:
                        if "ecl:" not in passport: #Check eye color field
                            continue
                        else:
                            if "pid:" not in passport: #Check passport id field
                                continue
                            else:
                                result1 = result1 + 1

print "Day 4 part 1 result : ", result1

#Day 4 part 2
#Validate valid passport