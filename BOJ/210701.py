from typing import List
import collections
import sys
input = sys.stdin.readline

# 2606 : 바이러스
com = input()
n = int(input())
graph = collections.defaultdict(list)
for _ in range(n):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node: int, route: List[int]) -> List[int]:
    route.append(node)
    for next in graph[node]:
        if next not in route:
            route = dfs(next, route)
    return route

if graph[1]:
    print(len(dfs(1,[]))-1)
else:
    print(0)

# 16953 : A -> B
a, b = map(int,input().split())

def calculate(target: int, num: int) -> int:
    cnt = 1
    while target < num:
        if num % 10 == 1:
            num = num // 10
            cnt += 1
        else:
            if num % 2 != 0:
                return -1
            else:
                num = num / 2
                cnt += 1
    return cnt if target == num else -1

print(calculate(a,b))
