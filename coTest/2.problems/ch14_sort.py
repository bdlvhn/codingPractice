import sys
input = sys.stdin.readline

def q23():
    n = int(input())
    students = []
    for _ in range(n):
        temp = list(input().split())
        temp[1:] = map(int, temp[1:])
        students.append(temp)

    return map(lambda x: x[0],
               sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0])))


# print(*q23(), sep='\n')

def q24():
    n = int(input())
    houses = [*map(int, input().split())]  # [5,1,7,9]
    houses.sort()

    return houses[(n - 1) // 2]


# print(q24())

def q25(N, stages):
    temp = []
    thisStage = len(stages)
    for i in range(1, N + 1):
        notClear = stages.count(i)
        if thisStage == 0:
            f = 0
        else:
            f = notClear / thisStage
        temp.append((i, f))
        thisStage -= notClear

    temp = sorted(temp, key=lambda x: (-x[1], x[0]))
    answers = map(lambda x: x[0], temp)

    return [*answers]


# print(q25(5, [2, 1, 2, 6, 2, 4, 3, 3]))

import heapq

def q26():
    n = int(input())
    numList = []
    for _ in range(n):
        numList.append(int(input()))
    heapq.heapify(numList)

    result = 0
    while len(numList) >= 2:
        a, b = heapq.heappop(numList), heapq.heappop(numList)
        result += (a + b)
        heapq.heappush(numList, a + b)
    return result


print(q26())