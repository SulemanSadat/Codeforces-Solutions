problems, time = map(int, input().split())
timeOfProblem = 0
Solved = 0
for problem in range(1, problems + 1):

    p = problem * 5
    timeOfProblem += p
    total = time + timeOfProblem
    if total <= 240:
        if problem == 1:
            timeOfProblem += 5
            Solved += 1
        if Solved < problems:
            Solved += 1

print(Solved)
