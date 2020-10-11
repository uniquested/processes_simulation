from classes.display import *


class RoundRobin:
    def __init__(self, processes, q, time, new):
        self.processes = processes
        self.q = q
        self.time = time
        self.new = new

    def RoundRobin(self, processes_list, q, Time, new):
        temp = []
        ready = []
        while len(processes_list) > len(new):
            for i in range(len(processes_list)):
                if processes_list[i][1] <= Time and processes_list[i][3] == 0:
                    processes_list[i][3] += 1
                    processes_list[i].append(0)
                    processes_list[i].append(0)
                    processes_list[i].append(0)
                    temp.insert(0, processes_list[i])
            temp0 = temp

            if len(temp0) > 0:
                for each in temp:
                    if each[3] == 1:
                        if each[7] == 0:
                            each[7] = each[1]
                        ready.append(each)

                ready.sort(key=lambda x: x[7])
                for each in ready:
                    ready.sort(key=lambda x: (x[6]))
                    temp.remove(each)
                    if each[0] - each[5] > q:
                        each[5] += q
                        Time += q
                        each[6] += 1
                        each[7] = Time
                    elif each[0] - each[5] == q:
                        each[5] += q
                        Time += q
                        each[3] += 1
                        each[2] = Time - each[1]
                        each[6] += 1
                        each[7] = Time
                    elif each[0] - each[5] < q and each[0] - each[5] > 0:
                        Time += each[0] - each[5]
                        each[5] = each[0]
                        each[3] += 1
                        each[2] = Time - each[1]
                        each[6] += 1
                        each[7] = Time
                    temp.append(each)
                    each[6] = 0
                ready.clear()
            else:
                temp2 = []
                for f in processes_list:
                    if f[3] == 0:
                        temp2.append(f)
                xyz = min(temp2, key=lambda x: x[1])[1]
                Time = xyz
                del temp2
            for l in temp:
                if l[3] == 2:
                    new.append(l)
                    l[3] = 3
                    temp0.remove(l)
        for i in new:
            i[2] -= i[0]
            i.pop()
            i.pop()
            i.pop()
        #new.sort(key=lambda x: x[1])


    def ExecuteTime(self, processes_list, q):
        for z in processes_list:
            z.append(z[0] + z[2])
        print("\nWyniki dla kwantu czasu = " + str(q))
        EndDisplay(processes_list, 0)
