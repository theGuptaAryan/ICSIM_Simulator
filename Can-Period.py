import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
participants = pd.read_csv("mixer.csv")
line =1
dict = {}
prevtime =0
time =0
channeldelay = {}
speed_count=0
for index, row in participants.iterrows():
    Data1 = row["Full"].title()

    # Code to check the periodicty before attacker starts sending messages:
    # if line>88000:
    #     break;
    # time1 = Data1[:]
    # #change this maybe
    # pos = time1.index('V')
    # time2 = time1[1:pos-2]
    # time = float(time2)
    # #change here to 25 for
    # Data = Data1[26:]
    # id = Data[:3]
    # if id=='244':
    #     speed_count = speed_count+1
    # if id in dict.keys():
    #     dict[id].append(line)
    #     channeldelay[id].append(time)
    # else:
    #     dict[id] = [line]
    #     channeldelay[id] = [time]
    # end here

    # Code to check the time period after the attacker starts sending messages!
    if line>88000:
        time1 = Data1[:]
       #change this maybe
        pos = time1.index('V')
        time2 = time1[1:pos-2]
        time = float(time2)
        #change here to 25 for
        Data = Data1[26:]
        if id == '244':
            speed_count = speed_count + 1
        id = Data[:3]
        if id in dict.keys():
            dict[id].append(line)
            channeldelay[id].append(time)
        else:
            dict[id] = [line]
            channeldelay[id] = [time]
    # end here

    line = line+1

print("Total CAN ID's: " + str(len(channeldelay)))

print(speed_count)

delay = {}
Idmean = {}
for id in channeldelay.keys():
    ls = channeldelay.get(id)
    diffLs = []
    n = len(ls)
    for i in range(n-1):
        diff = ls[i+1] - ls[i]
        newdiff = diff*1000
        newdiff1 = round(newdiff, 3)
        diffLs.append(newdiff1)
        if id in delay.keys():
            delay[id].append(newdiff1)
        else:
            delay[id] = [newdiff1]
    if(len(diffLs)<1):
        continue
    mean1 = sum(diffLs) / len(diffLs)
    mean = round(mean1,3)
    Idmean[id] = mean
    print(id+","+str(mean))


timep ={}
for m in Idmean.keys():
    me = Idmean.get(m)
    # print(m, me)
    added = False
    for t in timep.keys():
        dif = abs(t-me)/t
        if dif<0.06:
            w = timep.get(t)
            w.append(m)
            added = True
    if added==False:
        timep[me] = [m]

print(timep)

# X = []
# Y = []
# counter = 1
# for id in Idmean.keys():
#     if Idmean.get(id)<22:
#         Y.append(Idmean.get(id))
#         X.append(counter)
#     counter = counter+1
# plt.xlabel('Ids--->')
# plt.ylabel('Time Delay for Id message --> (ms)')
# # plt.plot(X, Y)
# plt.scatter(X, Y)
# plt.show()


X = []
Y = []
counter = 1
lgnd = []
for id in Idmean.keys():
    if Idmean.get(id)>250 and Idmean.get(id)<1200 :
        X = [id]
        Y = [Idmean.get(id)]
        lgnd.append(id)
        plt.scatter(X, Y)
    counter = counter+1
plt.xlabel('Ids--->')
plt.ylabel('Time Delay for Id message --> (ms)')
# plt.plot(X, Y)
plt.legend(lgnd)
plt.show()


# Plot graphs for a few particular Ids to plot their graph.
# X = []
# Y = []
# counter = 1
# for id in delay.keys():
#     n = len(delay.get(id))
#     for x in range(n):
#         X.append(counter)
#     for diff in delay.get(id):
#         # print(id+","+str(diff))
#         Y.append(diff)
#     counter = counter+1
# plt.xlabel('Ids--->')
# plt.ylabel('Time Delay for Id message --> (ms)')
# plt.plot(X, Y)
# plt.show()


# Plot graphs for a few particular Ids to plot their graph.
# X = []
# Y = []
# counter = 1
# lgnd = []
# for id in delay.keys():
#     print(id + ":  "+ str(counter))
#     n = len(delay.get(id))
#     X = np.linspace(1,(n-1),(n))
#     Y = delay.get(id)
#     # print(len(X), len(Y))
#     # plt.plot(X, Y)
#     # if counter==1 or counter==2 or counter==3 or counter==8 or counter==9 or counter==14 or counter==15 or counter==16 or counter==18 or counter==19 or counter==20:
#     #     lgnd.append(id)
#     #     plt.plot(X, Y)
#     if counter>0 and counter<5:
#         lgnd.append(id)
#         plt.plot(X, Y)
#     counter = counter+1
# plt.xlabel('No of messages of Id--->')
# plt.ylabel('Time Delay for Id message --> (ms)')
# plt.legend(lgnd)
# plt.show()