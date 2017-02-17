import psutil
import collections
from collections import *

a = psutil.net_connections(kind = 'tcp')

listOfPid = []
groupedList=[()]
list2 = [()]

for connection in range(len(a)):
    if(a[connection].laddr and a[connection].raddr):
        listOfPid2 = a[connection].pid
        listOfPid.append(listOfPid2)

        splittingladdr =  str(a[connection].laddr).split(',') #FormatedLaddrInRequiredFormat
        combiningladdr = splittingladdr[0].replace("\'","")+"@"+splittingladdr[1].strip()

        splittingraddr =  str(a[connection].raddr).split(',') #FormatedRaddrInRequiredFormat
        combiningraddr = splittingraddr[0].replace("\'","")+"@"+splittingraddr[1].strip()

        test1 = [(str(a[connection].pid) +"/"+combiningladdr+"/"+combiningraddr+"/"+str(a[connection].status),int(a[connection].pid))]
        list2=list2+test1 #FormattedListInRequiredFormat
del list2[0]

val_2=Counter([y for (x,y) in list2])
counterOfRecord = str(val_2).split('Counter')[1]
records = counterOfRecord.split(',') #Contains Records of all the items in the connection

ilist = []
for m in range(len(records)):
    if (int(m) == 0):
        firstItem = records[m][2:len(records[m])].strip()
        ilist2 = [firstItem]
        ilist.append(ilist2)
    elif (int(m) == len(records)-1):
        lastItem = records[m][0:-2].strip()
        ilist2= [lastItem]
        ilist.append(ilist2)
    else:
        otherItem = records[m].strip()
        ilist2 = [otherItem]
        ilist.append(ilist2)

myGroupedSortedDict = {}
for i in range(len(list2)):

    recordEbtry = list2[0]
    recordEntryFirstIndexElement = str(recordEbtry).split(',')
    pidList2 = str(list2[i]).split('/')[0][2:len(str(list2[i]).split('/')[0])]
    laddrValue = str(list2[i]).split('/')[1]
    raddrValue = str(list2[i]).split('/')[2]
    status = str(list2[i]).split('/')[3]
    formattedStatus = status[0:len(status)-len(pidList2)-4]


    for j in range(len(ilist)):
        pidInilist = ilist[j][0].split(':')[0]
        pidCountValue = int(ilist[j][0].split(':')[1].strip())
        if (int(pidInilist) == int(pidList2)):
            groupedTuple = [("\""+pidList2+ "\""+ ","+"\""+(laddrValue.replace("(","")).replace(")","") +"\""+ "," +"\""+ (raddrValue.replace("(","")).replace(")","")+ "\""+","+ "\""+formattedStatus+"\"", pidCountValue)]
            groupedList=groupedList+groupedTuple

del groupedList[0]
finalSortedOutput =  sorted(groupedList,key=lambda x: x[1], reverse= True)

print "\"pid\""+','+"\"laddr\""+','+ "\"raddr\""+','+"\"status\""
for k,v in finalSortedOutput:
    print k
