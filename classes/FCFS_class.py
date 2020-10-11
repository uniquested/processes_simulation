from classes.display import *


class FCFS:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    def Sort(self, processes_list, l):
        sort = sorted(processes_list, key=lambda x: x[1])
        # for i in range(0, l):
        #   for j in range(0, l-i-1):
        #       if (processes_list[j][1] > processes_list[j + 1][1]):
        #           tempo = processes_list[j]
        #          processes_list[j] = processes_list[j + 1]
        #         processes_list[j + 1] = tempo

    def ExecuteTime(self, processes_list):
        for z in processes_list:
            z.append(z[0] + z[2])
        EndDisplay(processes_list, 0)

    def WaitingTime(self, processes_list, Time):
        for f in processes_list:
            f[2] = Time - f[1]
            if f[2] <= 0:
                f[2] = 0
                Time = f[1]
            Time += f[0]
