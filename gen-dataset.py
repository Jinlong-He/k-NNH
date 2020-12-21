f = open('Gowalla_totalCheckins.data','r')
f15 = open('Gowalla_totalCheckins15.txt','w')
f16 = open('Gowalla_totalCheckins16.txt','w')
f17 = open('Gowalla_totalCheckins17.txt','w')
f18 = open('Gowalla_totalCheckins18.txt','w')
f19 = open('Gowalla_totalCheckins19.txt','w')
f20 = open('Gowalla_totalCheckins20.txt','w')
for line in f.readlines() :
    if ("2010-08-15" in line) :
        f15.write(line)
    if ("2010-08-16" in line) :
        f16.write(line)
    if ("2010-08-17" in line) :
        f17.write(line)
    if ("2010-08-18" in line) :
        f18.write(line)
    if ("2010-08-19" in line) :
        f19.write(line)
    if ("2010-08-20" in line) :
        f20.write(line)
f15.close() 
f16.close()
f17.close()
f18.close()
f19.close()
f20.close()

