import time
import datetime
f = open('Gowalla_totalCheckins.txt','r')
lines = f.readlines()
i = 1
l = len(lines)
for line in lines :
    args = line.split('\t')
    date = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(args[1], "%Y-%m-%dT%H:%M:%SZ"))).date()
    print(str(i) + "/" + str(l))
    i = i + 1
    fo = open (str(date) + '.txt', 'a')
    fo.write(line)
    fo.close()


