from classes.process import Process
from classes.SJF_class import *
from classes.FCFS_class import *
from classes.RoundRobin_class import *
from classes.Prirority_class import *
import os.path

while True:
    Time = 0
    problem = 0
    process_queue = list(map(int, []))
    process_list = list(map(int, []))
    TablicaZmienna = list(map(int, []))

    print("\n-------- SYMULACJA --------\n[1] - Wczytanie danych na początku programu"
          "\n[2] - Wczytanie danych z pliku\n[quit] - Zamknij program\n")

    case = str(input("Wybierz opcję: "))
    if case == "1":
        try:
            n = int(input("Proszę podać liczbę procesów: "))
        except ValueError:
            print("To nie jest liczba!")
            continue
        for i in range(n):
            bt, at, pr = input("Proszę podać długość procesu, "
                               "jego czas przybycia oraz priorytet (oddzielone spacją): ").split()
            try:
                process_list.insert(i, Process(int(bt), int(at), int(pr)))
            except ValueError:
                print("Źle wprowadzone dane!")
                problem = 1
                break
        if problem == 1:
            continue
        for i in process_list:
            process_queue.append(i.get_parameters())

    elif case == "2":
        file_name = input("Podaj nazwe pliku: ")
        if os.path.isfile(file_name) == False:
            print("Nie ma takiego pliku!")
            continue
        # otwarcie pliku
        with open(file_name, 'r') as p:
            n = int(p.readline())
            for i in range(n + 1)[1:]:
                try:
                    data1, data2, data3 = p.readline().split()
                except ValueError:
                    problem = 1
                    print("Błędnie zapisany plik")
                    break
                try:
                    process_list.insert(i, Process(int(data1), int(data2), int(data3)))
                except ValueError:
                    problem = 1
                    print("Błędnie zapisany plik")
                    break
            if problem == 1:
                continue
            p.close()
            for i in process_list:
                process_queue.append(i.get_parameters())

    elif case == "quit":
        quit()
    else:
        print("Błędna opcja!\n")
        continue

    print("\n[1] - Algorytm FCFS\n[2] - Algorytm SJF\n[3] - Algorytm Round Robin"
          "\n[4] - Algorytm priorytetowy FCFS\n[5] - Powrót do wyboru danych\n")

    second_case = str(input("Wybierz opcje: "))
    if second_case == "1":

        fcfs = FCFS(process_queue, n)

        fcfs.Sort(process_queue, n)

        fcfs.WaitingTime(process_queue, Time)

        fcfs.ExecuteTime(process_queue)

    elif second_case == "2":

        sjf = SJF(process_queue, TablicaZmienna)

        sjf.SJF_alg(process_queue, TablicaZmienna)

        sjf.WaitingTime(TablicaZmienna, Time)

        sjf.ExecuteTime(TablicaZmienna)

    elif second_case == "3":
        q = 3

        rr = RoundRobin(process_queue, q, Time, TablicaZmienna)

        rr.RoundRobin(process_queue, q, Time, TablicaZmienna)

        rr.ExecuteTime(TablicaZmienna, q)

    elif second_case == "4":

        pr = Prirority(process_queue, TablicaZmienna)

        pr.Prirority(process_queue, TablicaZmienna)

        pr.WaitingTime(TablicaZmienna, Time)

        pr.ExecuteTime(TablicaZmienna)

    elif second_case == "5":
        continue
    else:
        print("Błędna opcja")
