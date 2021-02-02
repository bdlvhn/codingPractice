# Q15 : 특정 거리의 도시 찾기
def q15():
  n,m,k,x = map(int,input().split())
  road = [[] for _ in range(n+1)]
  dist = [1e9]*(n+1)
  for _ in range(m):
    a,b = map(int,input().split())
    road[a].append(b)
  
  for i in road[x]:
    dist[i] = min(1,dist[i])  

  def departure(d,x):
    for j in road[x]: # x와 이어진 도시
      if road[j]:
        departure(d+1,j)
      else:
        dist[j] = min(d+1,dist[j])

  departure(0,x)

  cnt = 0
  for i,v in enumerate(dist):
    if v==k:
      print(i)
      cnt += 1
  if cnt == 0:
    print(-1)

# q15()

# Q16 : 연구소 (! 시간 초과)
from collections import deque
from itertools import combinations, chain
import copy
import time

start = 0

def q16():
  n,m = map(int,input().split()) # 입력
  global start
  start = time.time()

  board = [[-1]*(m+2) for _ in range(n+2)] # 판 생성
  virus = deque()
  cell = deque()
  answer = 0

  for i in range(n): # 판 이식
    a = list(map(int,input().split()))
    for j in range(m):
      board[i+1][j+1] = a[j]
      if a[j] == 0:
        cell.append([i+1,j+1])
      elif a[j] == 2:
        virus.append([i+1,j+1])

  cases = combinations(cell,3) # 경우의 수 생성
  route = {0:[-1,0],1:[1,0],2:[0,1],3:[0,-1]}

  def spread(board,virus): # 전염
    this_virus = copy.deepcopy(virus)
    while this_virus:
      v = this_virus.popleft()
      for d in range(4):
        x,y = v[0]+route[d][0],v[1]+route[d][1]
        if board[x][y] == 0:
          this_virus.append([v[0]+route[d][0],v[1]+route[d][1]])
          board[x][y] = 2
    return board

  def status(board): # 상태
    print("------------------")
    print("board : ")
    for row in board:
      print(row)
    print("------------------")

  for case in cases:
    new_board = copy.deepcopy(board)
    for c in case:
      new_board[c[0]][c[1]] = 1 # 벽 설치
    spread_board = spread(new_board,virus)
    res_board = list(chain(*spread_board))
    count = 0
    for i in res_board:
        if i == 0:
          count += 1 
    answer = max(count,answer)
    
  return answer

# print(q16())
# end = time.time()
# print(end-start)

def q17():
  n,k = map(int,input().split()) # 입력 정보
  s,x,y = map(int,input().split())
  board = []
  for _ in range(n):
    board.append(list(map(int,input().split())))
  virus_list = [None]*(k+1)

  for i in range(n): # 바이러스 시작점
    for j in range(n):
      if board[i][j] != 0:
        if virus_list[board[i][j]]:
          virus_list[board[i][j]].append([i,j])
        else:
          virus_list[board[i][j]] = [i,j]
  
  def spread(virus,infl): # 확산
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(4):
      nx = virus[0] + dx[i]
      ny = virus[1] + dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<n:
        if board[nx][ny] == 0:
          board[nx][ny] = infl
          virus_list[infl].append([nx,ny])

  cnt = 0
  while cnt<s: # s초간 반복
    for infl in range(1,k+1):
      if virus_list[infl]:
        for virus in virus_list[infl]:
          spread(virus,infl)
          virus_list[infl].pop(0)
  
  return board[x][y]

print(q17())
