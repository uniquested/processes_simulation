from classes.display import *


class SJF:
    def __init__(self, processes, new):
        self.processes = processes
        self.new = new


    def SJF_alg(self, processes_list, new):
        temp = []
        TimeSJF = 0
        while len(processes_list) != len(new):
            for f in processes_list:
                if f[1] <= TimeSJF and f[3] == 0:
                    temp.append(f)
            if len(temp) != 0:
                z = min(temp, key=lambda x: x[0])
                TimeSJF += z[0]
                processes_list.remove(z)
                temp.clear()
                new.append(z)
                z[3] += 1
                processes_list.append(z)
            else:
                temp2 = []
                for f in processes_list:
                    if f[3] == 0:
                        temp2.append(f)
                    xyz = min(temp2, key=lambda x: x[1])
                    TimeSJF = xyz[1]
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
        EndDisplay(processes_list, 0)