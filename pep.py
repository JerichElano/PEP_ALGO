def pep_formula(jobs, AT, BT, PR):
    n = len(jobs)
    WT = [0] * n
    TAT = [0] * n
    ET = [0] * n
    sequence = []
    t_sequence = [0]
    gantt_chart = []
    
    RP = list(PR)  # Remaining priority
    CT = 0  # Current time
    orig_BT = list(BT)  # Original burst times

    while True:
        MIN_PR = float('inf')  # Minimum priority
        MIN_BT = float('inf')  # Minimum burst time
        MIN_AT = float('inf')  # Minimum arrival time
        NJ = None  # Next job

        for i in range(n):
            if AT[i] <= CT and (RP[i], orig_BT[i], AT[i]) < (MIN_PR, MIN_BT, MIN_AT) and BT[i] > 0:
                MIN_PR = RP[i]
                MIN_BT = orig_BT[i]
                MIN_AT = AT[i]
                NJ = i

        if NJ is None:
            break

        BT[NJ] -= 1
        CT += 1

        sequence.append(jobs[NJ])

        if CT in AT:  # Appends arriving and finished jobs to the list t_sequence
            t_sequence.append(CT)
        elif BT[NJ] == 0:
            t_sequence.append(CT)

        if BT[NJ] == 0:
            WT[NJ] = CT - AT[NJ] - TAT[NJ] - orig_BT[NJ]
            ET[NJ] = CT
            TAT[NJ] = ET[NJ] - AT[NJ]
            RP[NJ] = float('inf')

    time_sequence = t_sequence  # To have a copy of data from t_sequence list

    while len(t_sequence) >= 2:  # Organizes the Gantt chart
        gantt_chart.append((sequence[0], t_sequence[1] - t_sequence[0]))  # Job, Duration of execution
        sequence = sequence[t_sequence[1] - t_sequence[0]:]  # Removes the first elements of sequence
        t_sequence = t_sequence[1:]  # Removes the first element of t_sequence

    return AT, orig_BT, PR, ET, TAT, WT, gantt_chart, time_sequence

def main():
    # AT, BT, PR = [], [], []

    # print("\n-------------------------------------")
    # print("CPU SCHEDULING | Preemptive Priority")
    # print("-------------------------------------\n")

    # n = int(input(f"Enter number of process: "))
    # jobs = [chr(ord('A') + i) for i in range(n)]
    
    # for i in range(n):
    #     AT.append(int(input(f"\nArrival Time (AT) of JOB {jobs[i]}: ")))
    #     BT.append(int(input(f"Burst Time (BT) of JOB {jobs[i]}: ")))
    #     PR.append(int(input(f"Priority (P) of JOB {jobs[i]}: ")))

    jobs = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    AT = [0, 0, 12, 22, 7, 27, 17, 3, 32]
    BT = [8, 6, 7, 6, 4, 3, 7, 6, 4]
    PR = [5, 5, 3, 1, 1, 3, 2, 4, 1]

    AT, BT, PR, ET, TAT, WT, gantt_chart, time_sequence = pep_formula(jobs, AT, BT, PR)
    
    print("\n\nG A N T T   C H A R T:")
    print("+-------" * len(gantt_chart), end='+\n')
    for process, duration in gantt_chart:
        print(f"|  {process}{duration} \t", end='')
    print("|")
    print("+-------" * len(gantt_chart), end='+\n')
    for time in time_sequence:
        print(f"{time}\t", end='')
    

    
    
    print("\n\n\nR  E  S  U  L  T:")
    print("+-------" * 7, end='+\n')
    print("| JOBS\t|   AT\t|   BT\t|   P\t|   ET\t|  TAT\t|  WT\t", end="|\n")
    print("+-------" * 7, end='+\n')
    for i in range(len(jobs)):
        print(f"|   {jobs[i]}\t|   {AT[i]}\t|   {BT[i]}\t|   {PR[i]}\t|   {ET[i]}\t|   {TAT[i]}\t|   {WT[i]}\t", end="|\n")
    print("+-------" * 7, end='+\n')

main()