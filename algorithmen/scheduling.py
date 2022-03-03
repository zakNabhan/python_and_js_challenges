'''
1-  Input the processes along with their burst time (bt).
2-  Find waiting time (wt) for all processes.
3-  As first process that comes need not to wait so
    waiting time for process 1 will be 0 i.e. wt[0] = 0.
4-  Find waiting time for all other processes i.e. for
     process i ->
       wt[i] = bt[i-1] + wt[i-1] .
5-  Find turnaround time = waiting_time + burst_time
    for all processes.
6-  Find average waiting time =
                 total_waiting_time / no_of_processes.
7-  Similarly, find average turnaround time =
                 total_turn_around_time / no_of_processes
'''

import numpy
def first_come_first(n, bt):
    wt=[]
    avgwt=0
    tat=[]
    avgtat=0
    wt.insert(0,0)
    tat.insert(0,bt[0])
    for i in range(1,len(bt)):
        wt.insert(i,wt[i-1]+bt[i-1])
        tat.insert(i,wt[i]+bt[i])
        avgwt+=wt[i]
        avgtat+=tat[i]
        avgwt=float(avgwt)/n
        avgtat=float(avgtat)/n
        print("\n")
    print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
    for i in range(0,n):
        print(str(i)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
        print("\n")

    print("Average Waiting time is: "+str(avgwt))
    print("Average Turn Arount Time is: "+str(avgtat))


print("\nWelcome to Scheduling Verfahren ")


def first_come_first_fun(n, bt):
    wt=[]
    avgwt=0
    tat=[]
    avgtat=0
    wt.insert(0,0)
    tat.insert(0,bt[0])
    for i in range(1,len(bt)):
        wt.insert(i,wt[i-1]+bt[i-1])
        tat.insert(i,wt[i]+bt[i])
        avgwt+=wt[i]
        avgtat+=tat[i]
        avgwt=float(avgwt)/n
        avgtat=float(avgtat)/n

    print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
    for i in range(0,n):
        print(str(i)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
        print("\n")

    return str(avgwt), str(avgtat)








def unbekannt(n, bt, wt=[],avgwt=0,tat=[], avgtat=0):
    # insert () mehtod insert the specified value at specified positio
    # list.insert(position, element)
    wt.insert(0,0) # hiert input the position 0 and the element 0 for waiting time
    #print("wt: ", wt)
    tat.insert(0,bt[0]) # hier wird erste burst_time index gespeichert z.b 24 4 4 ,
    #print("tat: ", tat)

    for i in range(1,len(bt)):
        #print("was ist I: ", i)# i gehen wir alle elemente  durch
        #print('lnge der bt',len(bt))
        wt.insert(i,wt[i-1]+bt[i-1])
        #print(i,wt[i-1]+bt[i-1])
        tat.insert(i,wt[i]+bt[i])
        #print(i, wt[i]+bt[i])


        print(numpy.mean(wt))
        print(numpy.mean(tat))


        '''
        avgwt= avgwt + wt[i]
        avgtat+=tat[i]
        avgwt=float(avgwt)/n
        avgtat=float(avgtat)/n
       '''

    print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
    for i in range(0,n):
        print(str(i)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
        print("\n")

    '''
    print("Average Waiting time is: "+str(avgwt))
    print("Average Turn Arount Time is: "+str(avgtat))
    '''



 
