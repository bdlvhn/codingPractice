import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right


def q27():
    n, x = map(int, input().split())
    numList = [*map(int, input().split())]
    numList.sort()
    l, r = bisect_left(numList, x), bisect_right(numList, x)
    return len(numList[l:r]) if numList[l:r] else -1


# print(q27())


def q28():
    n = int(input())
    array = [*map(int, input().split())]

    def binary_search(array, start, end):
        if start > end:
            return None
        mid = (start + end) // 2

        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            return binary_search(array, start, mid - 1)
        elif array[mid] < mid:
            return binary_search(array, mid + 1, end)

    idx = binary_search(array, 0, n - 1)

    if idx == None:
        print(-1)
    else:
        print(idx)


# q28()

import sys
input = sys.stdin.readline


def q29():
    n, c = map(int, input().split())

    houses = []
    for _ in range(n):
        houses.append(int(input()))
    houses.sort()

    start = 1
    end = houses[-1] - houses[0]
    result = 0

    while (start <= end):
        mid = (start + end) // 2
        value = houses[0]
        count = 1
        for i in range(1, n):
            if (houses[i] - value) >= mid:
                value = houses[i]
                count += 1
        if count >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)


# q29()


from bisect import bisect_left, bisect_right


def q30(words, queries):
    def count_by_range(l, left, right):
        a = bisect_right(l, right)
        b = bisect_left(l, left)
        return a - b

    word_array = [[] for _ in range(10000 + 1)]
    reversed_array = [[] for _ in range(10000 + 1)]

    answer = []

    for word in words:
        word_array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10000+1):
        word_array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[-1] == "?":
            answer.append(
                count_by_range(word_array[len(q)], q.replace('?', 'a'),
                               q.replace('?', 'z')))
        else:
            answer.append(
                count_by_range(reversed_array[len(q)],
                               q[::-1].replace('?', 'a'),
                               q[::-1].replace('?', 'z')))
    return answer