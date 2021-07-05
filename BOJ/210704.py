import collections
from collections import deque
import re
import sys
input = sys.stdin.readline

# 14226 : 이모티콘
# s = int(input())
# ch = [[-1]*(s+1) for _ in range(s+1)]
#
# def bfs():
#     de = deque()
#     de.append([1,0])
#     ch[1][0] = 0
#
#     while de:
#         x, y = de.popleft()
#
#         if ch[x][x] == -1:
#             ch[x][x] = ch[x][y] + 1
#             de.append([x,x])
#         if x+y <= s and ch[x+y][y] == -1:
#             ch[x+y][y] = ch[x][y] + 1
#             de.append([x+y,y])
#         if x-1 >= 0 and ch[x-1][y] == -1:
#             ch[x-1][y] = ch[x][y] + 1
#             de.append([x-1,y])
# bfs()
#
# r = ch[s][1]
# for i in range(1,s):
#     if ch[s][i] != -1:
#         r = min(r,ch[s][i])
# print(r)

# 17086 : 아기 상어 2
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# dx = (-1, -1, -1, 0, 0, 1, 1, 1)
# dy = (-1, 0, 1, -1, 1, -1, 0, 1)
# q = deque()
#
# def bfs():
#     while q:
#         x, y = q.popleft()
#         for k in range(8):
#             nx, ny = x+dx[k], y+dy[k]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if not a[nx][ny]:
#                 q.append((nx, ny))
#                 a[nx][ny] = a[x][y]+1
#
# for i in range(n):
#     for j in range(m):
#         if a[i][j]:
#             q.append((i, j))
# bfs()
# print(max(map(max, a))-1)

# 15486 : 퇴사 2
# n = int(input())
# t,p = [],[]
# dp = [0] * (n+1)
# for i in range(n):
#     x,y = map(int,input().split())
#     t.append(x)
#     p.append(y)
# M = 0
# for i in range(n):
#     M = max(M,dp[i])
#     if i+t[i] > n:
#         continue
#     dp[i+t[i]] = max(M+p[i], dp[i+t[i]])
# print(max(dp))

# 3568 : iSharp
# s = input().replace(',','')[:-1].split()
# p = re.compile('([a-zA-Z]+)([*\[\]&]*)')
#
# for j in range(1,len(s)):
#     m = p.search(s[j])
#     var = m.group(1)
#     body = m.group(2)
#     temp = s[0] + body[::-1].replace('][','[]') + ' ' + var + ';'
#     print(temp)
