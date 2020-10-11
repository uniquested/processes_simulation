
def EndDisplay(processes_list, z):
    s = " "
    total_waititme = 0
    total_executiontime = 0
    total_longtime = 0
    if z == 0:
        print("\nDługość procesu" + 10*s + "Czas wejścia" + 10*s
              + "Czas oczekiwania" + 10*s + "Czas wykonania procesu")
        for e in range(len(processes_list)):
            total_executiontime += processes_list[e][5]
            total_waititme += processes_list[e][2]
            total_longtime += processes_list[e][0]
            print("\t" + str(processes_list[e][0]) + "\t\t\t\t\t\t" + str(processes_list[e][1])
                  + "\t\t\t\t\t\t" + str(processes_list[e][2]) + "\t\t\t\t\t\t" + str(processes_list[e][5]))
    elif z == 1:
        print("\nDługość procesu" + 10 * s + "Czas wejścia" + 10 * s
              + "Czas oczekiwania" + 10 * s + "Czas wykonania procesu" + 10 * s + "Priorytet początkowy")
        for e in range(len(processes_list)):
            total_executiontime += processes_list[e][6]
            total_waititme += processes_list[e][2]
            total_longtime += processes_list[e][0]
            print("\t" + str(processes_list[e][0]) + "\t\t\t\t\t\t" + str(processes_list[e][1])
                  + "\t\t\t\t\t\t" + str(processes_list[e][2]) + "\t\t\t\t\t\t\t" + str(processes_list[e][6])
                  + "\t\t\t\t\t\t\t\t" + str(processes_list[e][5]))
    print("\nŚredni czas oczekiwania wynosi: " + str(round((total_waititme)/len(processes_list), 2)))
    print("\nŚredni czas wykonywania wynosi: " + str(round((total_executiontime) / len(processes_list), 2)))
    print("\nCałkowity czas trwania wynosi: " + str(total_longtime))
