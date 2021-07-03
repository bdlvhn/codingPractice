import collections
import sys
input = sys.stdin.readline

# 1697 : 숨바꼭질
# 12851 : 숨바꼭질 2
n, k = map(int,input().split())
array = [[-1,0] for _ in range(int(1e5)+1)]

def bfs(n: int):
    queue = collections.deque()
    queue.append(n)
    array[n][0] = 0
    array[n][1] = 1

    while queue:
        now = queue.popleft()

        for next in (now - 1, now + 1, now * 2):
            if 0 <= next <= int(1e5):
                if array[next][0] == -1:
                    array[next][0] = array[now][0] + 1
                    array[next][1] = array[now][1]
                    queue.append(next)
                elif array[next][0] == array[now][0] + 1:
                    array[next][1] += array[now][1]

bfs(n)
print(array[k][0],sep="\n")
print(array[k][1],sep="\n")

# 13549 : 숨바꼭질 3
n, k = map(int,input().split())
array = [[-1,0] for _ in range(int(1e5)+1)]

def bfs(n: int):
    queue = collections.deque()
    queue.append(n)
    array[n][0] = 0
    array[n][1] = 1

    while queue:
        now = queue.popleft()
        flash = now * 2
        if 0 <= flash <= int(1e5):
            if array[flash][0] == -1:
                array[flash][0] = array[now][0]
                array[flash][1] = array[now][1]
                queue.append(flash)
            elif array[flash][0] == array[now][0]:
                array[flash][1] += array[now][1]
        for next in (now - 1, now + 1):
            if 0 <= next <= int(1e5):
                if array[next][0] == -1:
                    array[next][0] = array[now][0] + 1
                    array[next][1] = array[now][1]
                    queue.append(next)
                elif array[next][0] == array[now][0] + 1:
                    array[next][1] += array[now][1]

bfs(n)
print(array[k][0],sep="\n")

# 13913 : 숨바꼭질 4
n, k = map(int,input().split())
array = [[-1,-1] for _ in range(int(1e5)+1)]

def bfs(n: int):
    queue = collections.deque()
    queue.append(n)
    array[n][0] = 0

    while queue:
        now = queue.popleft()

        if now == k:
            return array[k][0]

        for next in (now - 1, now + 1, now * 2):
            if 0 <= next <= int(1e5):
                if array[next][0] == -1:
                    array[next][0] = array[now][0] + 1
                    array[next][1] = now
                    queue.append(next)

print(bfs(n))

route = collections.deque()
route.append(k)

while 1:
    if array[k][1] != -1:
        route.appendleft(array[k][1])
        k = array[k][1]
    else:
        break

print(*route)