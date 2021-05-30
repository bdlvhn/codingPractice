import sys
input = sys.stdin.readline
INF = int(1e9)

def q01():
    n = int(input())
    guild = [*map(int, input().split())]
    guild.sort()

    result = 0
    count = 0

    for person in guild:
        count += 1
        if count >= person:
            result += 1
            count = 0

    return result

# print(q01())

def q02():
    number = [int(n) for n in input().rstrip()]
    result = number[0]

    for i in range(1, len(number)):
        result = max(result + number[i], result * number[i])

    return result

# print(q02())

def q03():
    string = input().rstrip()
    cnt = 0
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            cnt += 1
    return cnt // 2 + cnt % 2

# print(q03())

def q04():
    n = int(input())
    coins = [*map(int, input().split())]
    coins.sort()
    target = 1

    for coin in coins:
        if target < coin:
            return target
        else:
            target += coin

# print(q04())

def q05():
    n, m = map(int, input().split())
    balls = [*map(int, input().split())]
    array = [0] * (10 + 1)

    for x in balls:
        array[x] += 1

    result = 0
    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n

    return result

# print(q05())

import heapq

def q06(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


# food_times = [3, 1, 2]
# k = 5
# print(q06(food_times, k))