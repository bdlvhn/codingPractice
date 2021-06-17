import sys
input = sys.stdin.readline
import collections
from typing import List

#1260 : DFS 와 BFS
# vertex, edge, start = map(int,input().split())
# graph = collections.defaultdict(list)
# visited = collections.defaultdict(int)
# for _ in range(edge):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# for node in graph:
#     graph[node].sort()
#
# def dfs(node: int, route: List[int]) -> List[int]:
#     route.append(node)
#     for next in graph[node]:
#         if next not in route:
#             route = dfs(next, route)
#     return route
#
# def bfs(node:int) -> List[int]:
#     route = []
#     queue = collections.deque()
#     queue.append(node)
#     route.append(node)
#
#     while queue:
#         now = queue.popleft()
#         for next in graph[now]:
#             if next not in route:
#                 route.append(next)
#                 queue.append(next)
#     return route
#
# print(' '.join(map(str,dfs(start,[]))))
# print(' '.join(map(str,bfs(start))))

# 1303 : 전쟁 - 전투
n, m = map(int,input().split())
board = []
for _ in range(m):
    board.append([*input().rstrip('\n')])
answer = collections.defaultdict(int)

visited = [[False]*n for _ in range(m)]
def dfs(x: int, y: int, person: int):
    visited[x][y] = True
    person += 1
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n and \
            not visited[nx][ny] and (board[x][y] == board[nx][ny]):
            person = dfs(nx,ny,person)
    return person

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            answer[board[i][j]] += dfs(i,j,0)**2

print(answer['W'],answer['B'],sep=' ')

