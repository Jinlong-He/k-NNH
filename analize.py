import matplotlib.pyplot as plt
import numpy as np
f = open('result.txt', 'r')
k_dict = {1:{}, 2:{}, 3:{}, 5:{}, 10:{}, 100:{}}
year_months = []
for line in f.readlines() :
    datas = line[21:].split(',')
    year = line[15:19]
    month = int(datas[0])
    k = int(datas[2])
    acc = float(datas[3])
    time = float(datas[4][:len(datas[4])-2])
    data_dict = k_dict[k]
    if (not data_dict.__contains__((year, month))) :
        data_dict[(year, month)] = [acc, time, 1]
        if (k == 1) :
            year_months.append(year[2:] + '-' + str(month))
    else :
        data_dict[(year, month)][0] = data_dict[(year, month)][0] + acc
        data_dict[(year, month)][1] = data_dict[(year, month)][1] + time 
        data_dict[(year, month)][2] = data_dict[(year, month)][2] + 1
acc_ks = {1:[], 2:[], 3:[], 5:[], 10:[], 100:[]}
time_ks = {1:[], 2:[], 3:[], 5:[], 10:[], 100:[]}
for (k, data_dict) in k_dict.items() :
    for (year_month, data) in data_dict.items() :
        acc_ks[k].append(data[0]/data[2])
        time_ks[k].append(data[1]/data[2])
plt.figure(figsize=(12,6),dpi=80)
l1 = plt.plot(year_months, acc_ks[1], c='red', marker='*', label='k=1')
l2 = plt.plot(year_months, acc_ks[2], c='green', marker='s', label='k=2')
l3 = plt.plot(year_months, acc_ks[3], c='blue', marker='^', label='k=3')
l5 = plt.plot(year_months, acc_ks[5], c='gold', marker='v', label='k=5')
l10 = plt.plot(year_months, acc_ks[10], c='black', marker='+', label='k=10')
l100 = plt.plot(year_months, acc_ks[100], c='purple', marker='p', label='k=100')
plt.ylim(0.7, 1.0)
plt.ylabel('Accuracy')
plt.xlabel('year-month')
plt.legend()
plt.savefig('acc.png')
plt.show()

plt.figure(figsize=(12,6),dpi=80)
t1 = plt.plot(year_months, time_ks[1], c='red', marker='*', label='k=1')
t2 = plt.plot(year_months, time_ks[2], c='green', marker='s', label='k=2')
t3 = plt.plot(year_months, time_ks[3], c='blue', marker='^', label='k=3')
t5 = plt.plot(year_months, time_ks[5], c='gold', marker='v', label='k=5')
t10 = plt.plot(year_months, time_ks[10], c='black', marker='+', label='k=10')
t100 = plt.plot(year_months, time_ks[100], c='purple', marker='p', label='k=100')
#plt.ylim(0.7, 1.0)
plt.ylabel('Time')
plt.xlabel('year-month')
plt.legend()
plt.savefig('time.png')
plt.show()
