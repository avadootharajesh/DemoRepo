
# Job Sequencing with Deadlines

class Job:
    def __init__(self, jobid, deadline, profit):
        self.jobid = jobid
        self.deadline = deadline
        self.profit = profit
def jobseqencing(jobs, maxdeadline):
    jobs.sort(key = lambda x: x.profit, reverse = True)
    slots = [-1] * maxdeadline
    profit = 0
    seq = []
    for i in jobs:
        for j in range(min(i.deadline, maxdeadline) - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = i.jobid
                profit += i.profit
                seq.append(i.jobid)
                break
    return profit, seq

jobs = [Job(1, 2, 100), Job(2, 1, 19), Job(3, 2, 27), Job(4, 1, 25), Job(5, 3, 15)]
maxdeadline = 3
profit, seq = jobseqencing(jobs, maxdeadline)
print(profit)
print(seq)