from classes.display import *


class Prirority:
    def __init__(self, processes, new):
        self.processes = processes
        self.new = new

    def Prirority(self, processes_list, new):
        temp = []
        counter = 0
        prirority_time = 0
        while len(processes_list) > len(new):
            if counter == 0:
                for i in processes_list:
                    i.append(i[4])
                counter += 1
            for i in processes_list:
                if i[1] <= prirority_time and i[3] == 0:
                    temp.append(i)
            if len(temp) > 0:
                for l in range(len(temp)):
                    prirority_add = prirority_time - temp[l][1] + temp[l][5]
                    temp[l][4] = prirority_add
                    del prirority_add
                maxi = sorted(temp, key=lambda x: x[4], reverse=True)
                for i in maxi:
                    processes_list.remove(i)
                maxi[0][3] += 1
                prirority_time += maxi[0][0]
                for i in temp:
                    processes_list.append(i)
                new.append(maxi[0])
                temp.clear()

            else:
                temp2 = []
                for p in processes_list:
                    if p[3] == 0:
                        temp2.append(p)
                xyz = min(temp2, key=lambda x: x[1])
                prirority_time = xyz[1]
                del temp2

    def WaitingTime(self, processes_list, Time):
        for f in processes_list:
            f[2] = Time - f[1]
            if f[2] <= 0:
                f[2] = 0
                Time = f[1]
            Time += f[0]

    def ExecuteTime(self, processes_list):
        for z in processes_list:
            z.append(z[0] + z[2])
        EndDisplay(processes_list, 1)