from collections import deque

n = int(input("Enter number of processes: "))
bt = []

for i in range(n):
    burst = int(input(f"Enter Burst Time for P{i+1}: "))
    bt.append(burst)

quantum = int(input("Enter Time Quantum: "))

if quantum <= 0 or any(b <= 0 for b in bt):
    raise ValueError("Burst times and quantum must be positive.")

remaining = bt.copy()
wt = [0] * n
tat = [0] * n
completion = [0] * n

queue = deque(range(n))
time = 0

while queue:
    i = queue.popleft()

    execution = min(quantum, remaining[i])
    time += execution
    remaining[i] -= execution

    if remaining[i] > 0:
        queue.append(i)
    else:
        completion[i] = time
        tat[i] = completion[i]
        wt[i] = tat[i] - bt[i]

print("\nProcess\tBT\tWT\tTAT")

for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

print("\nAverage Waiting Time:", sum(wt)/n)
print("Average Turnaround Time:", sum(tat)/n)