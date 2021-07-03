import sys
input = sys.stdin.readline

# 2178 : 미로 탐색
# n, m = map(int, input().split())
# board = []
# queue = []
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# for i in range(n):
#     board.append(list(input().rstrip()))
# queue = collections.deque()
# queue.append((0,0))
# board[0][0] = 1
# while queue:
#     a,b = queue.popleft()
#     for i in range(4):
#         nx = a + dx[i]
#         ny = b + dy[i]
#         if (0 <= nx < n) and (0 <= ny < m) and board[nx][ny] == '1':
#             queue.append([nx, ny])
#             board[nx][ny] = board[a][b] + 1
# print(*board,sep='\n')
# print(board[n - 1][m - 1])

# 1743 : 음식물 피하기
# DFS
import sys
sys.setrecursionlimit(1000000)

def DFS(y, x):
    global field, dy, dx, N, M, comp

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and field[ny][nx]:
            field[ny][nx] = 0
            comp += 1
            DFS(ny, nx)

N, M, K = map(int, input().split())
field = [[0 for i in range(M)] for j in range(N)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(K):
    r, c = map(int, input().split())
    field[r - 1][c - 1] = 1

size = -1
for i in range(N):
    for j in range(M):
        if field[i][j]:
            field[i][j] = 0
            comp = 1
            DFS(i, j)
            size = max(comp, size)

print(size)

# BFS
from collections import deque


def BFS(r, c):
    global N, M, field
    q = deque([(r, c)])
    field[r][c] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    size = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and field[ny][nx]:
                q.append((ny, nx))
                field[ny][nx] = 0
                size += 1

    return size


N, M, K = map(int, input().split())
field = [[0 for i in range(M)] for j in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    field[r - 1][c - 1] = 1

size = -1
for i in range(N):
    for j in range(M):
        if field[i][j]:
            size = max(size, BFS(i, j))

print(size)