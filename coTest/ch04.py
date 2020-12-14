import time

### Ch04, 예제 4-1: 상하좌우
def solution_01():
  n = int(input())
  plan = input().split(" ")
  loc = [1,1]
  loc_dict = {"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}
  
  global start_time
  start_time = time.time()

  for d in plan:
    loc = [a+b for a,b in zip(loc,loc_dict[d])]
    if loc[0]>n:
      loc[0]=n
    elif loc[0]<1:
      loc[0]=1
    
    if loc[1]>n:
      loc[1]=n
    elif loc[1]<1:
      loc[1]=1
  
  return ' '.join(list(map(str,loc)))

# print(solution_01())
# end_time = time.time()
# print("excuted time: ",end_time-start_time)



### Ch04, 예제 4-2: 시각
def solution_02():
  n = int(input())
  cnt = 0

  global start_time
  start_time = time.time()

  for i in range(n+1):
    for j in range(60):
      for k in range(60):
        if '3' in str(i)+str(j)+str(k):
          cnt+=1
  
  return cnt

# print(solution_02())
# end_time = time.time()
# print("excuted time: ",end_time-start_time)



### Ch04, 4-2: 왕실의 나이트
def solution_03():
  n = input()
  loc = [int(ord(n[0]))-int(ord('a')),int(n[1])]
  cnt = 0

  global start_time
  start_time = time.time()

  cases = [[2,1],[2,-1],[-2,1],[-2,-1],
           [1,2],[1,-2],[-1,2],[-1,-2]]

  for case in cases:
    result = [a+b for a,b in zip(loc,case)]
    if result[0] > 0 & result[0] < 9 & result[1] > 0 & result[1] < 9:
      cnt += 1

  return cnt

# print(solution_03())
# end_time = time.time()
# print("excuted time: ",end_time-start_time)



### Ch04, 4-3: 게임 개발
n, m = map(int,input().split(" "))
x, y, direction = map(int,input().split(" "))
d = [[0]*m for _ in range(n)]
d[x][y]=1

board = []
for i in range(n):
  board.append(list(map(int,input().split())))

dx, dy = [-1,0,1,0], [0,1,0,-1]

def turn_left():
  global direction
  direction = (direction-1)%4

count = 1
turn_time = 0
while True:
  turn_left()
  nx, ny = x + dx[direction], y + dy[direction]

  if d[nx][ny] == 0 and board[nx][ny]==0:
    x,y = nx,ny
    d[x][y] = 1
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1
  
  if turn_time==4:
    nx, ny = x - dx[direction], y - dy[direction]
    if board[nx][ny]==0:
      x, y = nx, ny
    else:
      break
    turn_time = 0

print(count)
