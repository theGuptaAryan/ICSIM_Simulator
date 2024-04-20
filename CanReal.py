import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
participants = pd.read_csv("Real.csv")
line =1
dict = {}
channeldelay = {}
for index, row in participants.iterrows():
    Data1 = row["Full"].title()
    pos = Data1.find(",")
    pos1 = Data1.find(",", pos+1)
    diff = float(Data1[pos+1:pos1])
    pos3 = Data1.find("I")
    id = Data1[pos3+4:pos3+7]
    # print(id)
    # print(diff)
    if id in channeldelay.keys():
        dict[id].append(line)
        channeldelay[id].append(diff)
    else:
        dict[id] = [line]
        channeldelay[id] = [diff]
    line = line+1


#voltage fingerprint check

# for dd in channeldelay.keys():
#     ls = channeldelay.get(dd)
#     print(dd+ " " + str(ls))


print("Total CAN ID's: " + str(len(channeldelay)))

means = {}
wholesum =0
for rows in dict.keys():
    # print(rows, dict.get(rows))
    diff = []
    s= dict.get(rows)
    n = len(dict.get(rows))
    if n==1:
        print("only one", rows)
        diff = s
    else:
        for x in range(0,n-1):
            diff.append(s[x+1]-s[x])
        # print(diff)
    mean = sum(diff) / len(diff)
    variance = sum([((x - mean) ** 2) for x in diff]) / len(diff)
    std = variance ** 0.5
    #print("For id: "+ str(rows)+"       mean: "+ str(round(mean,3)) + "        standard deviation: " + str(round(std,5)))
    means[rows] = round(mean,0)
    diff.sort()
    a1 = diff[0]
    al = diff[len(diff)-1]
    # print(a1, al)
    mean = round(mean)
    max_diff = max((mean-a1),(al-mean))
    # print(max_diff)
    wholesum = wholesum + n
    # print("ID: "+rows+"     Mean time period of CAN samples: "+ str(mean)+"      Max Can msg deviation: " + str(max_diff) + "      Total ID messages: " + str(n))

delay = {}
for id in channeldelay.keys():
    ls = channeldelay.get(id)
    for diff in ls:
        newdiff = diff*100000
        newdiff1 = round(newdiff, 3)
        if id in delay.keys():
            delay[id].append(newdiff1)
        else:
            delay[id] = [newdiff1]
# X = []
# Y = []
# counter = 1
# for id in delay.keys():
#     n = len(delay.get(id))
#     for x in range(n):
#         X.append(counter)
#     for diff in delay.get(id):
#         print(id+","+str(diff))
#         Y.append(diff)
#     counter = counter+1
# plt.xlabel('Ids--->')
# plt.ylabel('Time Delay for Id message --> (*10^-5 seconds)')
# plt.plot(X, Y)
# plt.show()


X = []
Y = []
counter = 1
lgnd = []
for id in delay.keys():
    print(id + ":  "+ str(counter))
    n = len(delay.get(id))
    X = np.linspace(1,(n-1),(n))
    Y = delay.get(id)
    # print(len(X), len(Y))
    # plt.plot(X, Y)
    # if counter==1 or counter==2 or counter==3 or counter==8 or counter==9 or counter==14 or counter==15 or counter==16 or counter==18 or counter==19 or counter==20:
    #     lgnd.append(id)
    #     plt.plot(X, Y)
    if counter>21 and counter<36:
        lgnd.append(id)
        plt.plot(X, Y)
    counter = counter+1
plt.xlabel('No of messages of Id--->')
plt.ylabel('Time Delay for Id message --> (*10^-5 seconds)')
plt.legend(lgnd)
plt.show()
