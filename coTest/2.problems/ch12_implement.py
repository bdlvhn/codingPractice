# Ch12, 구현 문제

# Q7 : 럭키 스트레이트
def ch12_q07():
  n = input()
  return 'LUCKY' if sum(map(int,n[:int(len(n)/2)]))==sum(map(int,n[-int(len(n)/2):])) else 'READY'

# print(ch12_q07())

# Q8 : 문자열 재정렬
def ch12_q08():
  s = input()
  alpha_list, num_list = [], []
  for chr in s:
    if chr.isalpha():
      alpha_list.append(chr)
    else:
      num_list.append(int(chr))
  return ''.join(sorted(alpha_list)) + str(sum(num_list))

# print(ch12_q08())

# Q9 : 문자열 압축
def ch12_q09():
  s = input()
  min_len = len(s)

  for i in range(1,len(s)//2+1):
    this_len = 0
    cnt = 0
    lst = list(map(''.join, zip(*[iter(s)]*i)))
    print(lst)
    for j in range(len(lst)-1):
      if (lst[j]==lst[j+1]) & cnt == 0:
        this_len += i + 1
        cnt += 1
      elif (lst[j]==lst[j+1]) & cnt != 0:
        this_len += i
        cnt += 1
      else:
        cnt = 0
        this_len += i
    min_len = min(min_len,this_len)
    print(min_len,i)
  
  return min_len

# print(ch12_q09())

# Q10 : 자물쇠와 열쇠
import copy
def ch12_q10():
  key,lock = [[0,0,0],[1,0,0],[0,1,1]], [[1,1,0],[1,1,0],[1,0,1]]
  answer = [[1]*len(lock) for _ in range(len(lock))]

  zero_mat = [[0]*len(lock)*3 for _ in range(len(lock)*3)]
  for i in range(len(lock)):
    for j in range(len(lock)):
      zero_mat[i+len(lock)][j+len(lock)] = lock[i][j]


  def print_mat(mat):
    print("---------------")
    for row in mat:
      print(row)
    print("---------------")

  def mat_sum(x,y):
    return ([[c+d for c,d in zip(a,b)] for a,b in zip(x,y)])

  def mat_rotate(mat):
    return [list(a[::-1]) for a in zip(*mat)]
  
  for h in range(4):
    key = mat_rotate(key)
    for i in range(1,2*len(lock)):
      for j in range(1,2*len(lock)):
        tmp_mat = copy.deepcopy(zero_mat)
        sum_mat = mat_sum(key,[a[j:j+len(lock)] for a in tmp_mat[i:i+len(lock)]])
        for k in range(len(key)):
          tmp_mat[i+k][j:j+len(key)] = sum_mat[k]
        if [a[len(lock):2*len(lock)] for a in tmp_mat[len(lock):2*len(lock)]] == answer:
          return True
  
  return False

# print(ch12_q10())

# Q11 : 뱀
def ch12_q11():
  n = int(input()) # 보드 크기
  k = int(input()) # 사과 갯수
  apple = []
  for _ in range(k): # 사과 위치 입력
    x,y = map(int,input().split()) 
    apple.append([x-1,y-1])

  chg = [0]*(10000+1)
  l = int(input()) # 방향 전환 갯수
  for _ in range(l): # 방향 전환 입력
    x,c = input().split()
    if c == 'L':
      chg[int(x)] = -1
    elif c == 'D':
      chg[int(x)] = 1

  dict = [[0,-1],[-1,0],[0,1],[1,0]] # 좌,상,우,하 순
  head, tail = [0,0], [] # 머리, 꼬리
  dir = 2 # 방향 - 우로 시작
  
  time = 0
  print("time :",time," head: ",head," tail: ",tail," apple: ",apple,"dir: ",dir)
  while 1:
    time += 1 # 시간 경과
    head = [a+b for a,b in zip(head,dict[dir])] # 1. 머리 전진

    if head[0]<0 or head[0]>=n or head[1]<0 or head[1]>=n: # 종료 1 : 장외일 때 끝
      return time

    tail.insert(0,[a-b for a,b in zip(head,dict[dir])])

    if head in tail: # 종료 2 : 자기 몸에 부딪힐 때 끝
      return time

    if head in apple: # 2. 사과 있을 경우
      apple.remove(head)
    else: # 3. 사과 없을 경우
        tail.pop()
    
    print("time :",time," head: ",head," tail: ",tail," apple: ",apple,"dir: ",dir)

    if head in tail: # 종료 2 : 자기 몸에 부딪힐 때 끝
      return time

    if chg[time]!=0: # 방향 전환 수행
      dir = (dir + chg[time]) % 4

# print(ch12_q11())

# Q12 : 기둥과 보 설치
n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1], # case 1
#                [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1], # case 2
               [2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
board = [[0] * (n+1) for _ in range(n+1)] # 판 생성

def ch12_q12(n,build_frame):

  for step in build_frame: # 각 과정 실행
    x,y = step[0], step[1]
    st = step[2] # 0 : 기둥(ㅣ,2), 1 : 보(ㅡ,4)
    op = step[3] # 0 : 삭제, 1 : 설치

    if op == 1: # 설치
      if st == 0 and (y == 0 or board[x][y] in (2,4)): # 기둥 설치
        board[x][y] += 2
        board[x][y+1] += 2
      elif st == 1 and (board[x][y] == 2 or board[x+1][y] == 2) or (board[x][y] == 4 and board[x+1][y] == 4) : # 보 설치
        board[x][y] += 4
        board[x+1][y] += 4
    elif op == 0: # 삭제
      if st == 0:
        board[x][y] -= 2
        board[x][y+1] -= 2
        if not (y == 0 or board[x][y] in (2,4)):
          board[x][y] += 2
          board[x][y+1] += 2
      elif st == 1:
        board[x][y] -= 4
        board[x+1][y] -= 4
        if not ((board[x][y] == 2 or board[x+1][y] == 2) or (board[x][y] == 4 and board[x+1][y] == 4)):
          board[x][y] += 4
          board[x+1][y] += 4
         
  for row in [list(a) for a in zip(*board)][::-1]: # 프린트
    print(row)

  result = []
  for i in range(n+1): # 결과 넣기
    for j in range(n+1):
      if board[i][j]==2:
        result.append([i,j,0])
        board[i][j]-=2
        board[i][j+1]-=2
      elif board[i][j]==4:
        result.append([i,j,1])
        board[i][j]-=4
        board[i+1][j]-=4
  
  for row in [list(a) for a in zip(*board)][::-1]: # 프린트
    print(row)

  return sorted(result,key=lambda x:(x[0],x[1],x[2]))

# print(ch12_q12(n,build_frame))

# Q13 : 치킨 배달
from itertools import combinations
def ch12_q13():
  n,m = map(int,input().split()) # n, m 입력
  city = []
  for _ in range(n): # 도시 정보
    city.append(list(map(int,input().split())))
  
  house, chicken = [], []
  
  for i in range(n): # 집, 치킨집 정보 넣기
    for j in range(n):
      if city[i][j] == 1:
        house.append(([i,j]))
      elif city[i][j] == 2:
        chicken.append([i,j])
  
  def calculate(house,chicken):
    inf = int(1e9)
    min_cost = [inf] * len(house)
    for i in range(len(chicken)):
      for j in range(len(house)):
        cost = sum([abs(a-b) for a,b in zip(chicken[i],house[j])])
        min_cost[j] = min(min_cost[j],cost)
    return sum(min_cost)

  for m in range(m):
    result = int(1e9)
    this_chicken = list(combinations(chicken,m+1))
    for c in this_chicken:
      cost = calculate(house,c)
      result = min(result,cost)
  
  return result

  def print_city(): # 도시 프린트 함수
    print("도시 : ")
    for row in city:
      print(row)
    print("집 : ",house)
    print("치킨집 : ",chicken)
    print("코스트 : ",cost)
  
# print(ch12_q13())

# Q14 : 외벽 점검
from itertools import combinations
n, weak, dist = 12, [1,5,6,10], [1,2,3,4]
def ch12_q14(n,weak,dist):
  print([elm for elm in list(combinations(weak,2))])
  return [min((a-b)%n,(b-a)%n) for a,b in [elm for elm in list(combinations(weak,2))]]

print(ch12_q14(n,weak,dist))


###############################
### answer code on the book ###
###############################

# Q7 : 럭키 스트레이트
def ch12_q07b():
  n = input()
  length = len(n)
  summary = 0

  for i in range(length//2):
    summary += int(n[i])
  for i in range(length//2,length):
    summary -= int(n[i])
  
  if summary == 0:
    return 'LUCKY'
  else:
    return 'READY'

# Q8 : 문자열 재정렬
def ch12_q08b():
  data = input()
  result = []
  value = 0

  for x in data:
    if x.isalpha():
      result.append(x)
    else:
      value += int(x)
  result.sort()
  if value!=0:
    result.append(str(value))
  
  return ''.join(result)

# Q9 : 문자열 압축
def ch12_q09b(s):
  answer = len(s)

  for step in range(1,len(s)//2+1):
    compressed = ""
    prev = s[0:step]
    count = 1
    
    for j in range(step,len(s),step):
      if prev == s[j:j+step]:
        count += 1
      else:
        compressed += str(count) + prev if count>=2 else prev
        prev = s[j:j+step]
        count = 1
    compressed += str(count) + prev if count>=2 else prev
  
  answer = min(answer.len(compressed))

  return answer
  
# Q10 : 자물쇠와 열쇠
def ch12_q10b(key,lock):
  def rotate_a_matrix_by_90_degree(a):
    n, m = len(a), len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
      for j in range(m):
        result[j][n-i-1]=a[i][j]
    return result

  def check(new_lock):
    lock_length = len(new_lock)
    for i in range(lock_length,lock_length*2):
      for j in range(lock_length,lock_length*2):
        if new_lock[i][j] != 1:
          return False
    return True
  
  def solution():
    n, m = len(lock), len(key)
    new_lock = [[0]* (n*3) for _ in range(n*3)]

    for i in range(n):
      for j in range(n):
        new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
      key = rotate_a_matrix_by_90_degree(key)
      for x in range(n*2):
        for y in range(n*2):
          for i in range(m):
            for j in range(m):
              new_lock[x+i][y+j]+=key[i][j]
          if check(new_lock)==True:
            return True
          for i in range(m):
            for j in range(m):
              new_lock[x+i][y+j] -= key[i][j]
    return False

# Q11 : 뱀
def ch12_q11b():
  n = int(input())
  k = int(input())
  data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
  info = [] # 방향 회전 정보

  # 맵 정보(사과 있는 곳은 1로 표시)
  for _ in range(k):
      a, b = map(int, input().split())
      data[a][b] = 1

  # 방향 회전 정보 입력
  l = int(input())
  for _ in range(l):
      x, c = input().split()
      info.append((int(x), c))

  # 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  def turn(direction, c):
      if c == "L":
          direction = (direction - 1) % 4
      else:
          direction = (direction + 1) % 4
      return direction

  def simulate():
      x, y = 1, 1 # 뱀의 머리 위치
      data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
      direction = 0 # 처음에는 동쪽을 보고 있음
      time = 0 # 시작한 뒤에 지난 '초' 시간
      index = 0 # 다음에 회전할 정보
      q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

      while True:
          nx = x + dx[direction]
          ny = y + dy[direction]
          # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
          if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
              # 사과가 없다면 이동 후에 꼬리 제거
              if data[nx][ny] == 0:
                  data[nx][ny] = 2
                  q.append((nx, ny))
                  px, py = q.pop(0)
                  data[px][py] = 0
              # 사과가 있다면 이동 후에 꼬리 그대로 두기
              if data[nx][ny] == 1:
                  data[nx][ny] = 2
                  q.append((nx, ny))
          # 벽이나 뱀의 몸통과 부딪혔다면
          else:
              time += 1
              break
          x, y = nx, ny # 다음 위치로 머리를 이동
          time += 1
          if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
              direction = turn(direction, info[index][1])
              index += 1
      return time

# Q12 : 기둥과 보 설치
def ch12_q12b():
  def possible(answer):
    for x,y,stuff in answer:
      if stuff == 0:
        if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
          continue
        return False
      elif stuff == 1:
        if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
          continue
        return False
    return True

    def solution(n,build_frame):
      answer = []
      for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0:
          answer.remove([x,y,stuff])
          if not possible(answer):
            answer.append([x,y,stuff])
        if operate == 1:
          if not possible(answer):
            answer.remove([x,y,stuff])
      return sorted(answer)
      
# Q13 : 치킨 배달
from itertools import combinations
def ch12_q13b():
  n,m = map(int,input().split())
  chicken,house = [],[]

  for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
      if data[c]==1:
        house.append((r,c))
      elif data[c]==2:
        chicken.append((r,c))

  candidates = list(combinations(chicken,m))

  def get_sum(candidate):
    result = 0
    for hx,hy in house:
      temp = 1e9
      for cx,cy in candidate:
        temp = min(temp,abs(hx-cy)+abs(hy-cy))
      result += temp
    return result

  result = 1e9
  for candidate in candidates:
    result = min(result,get_sum(candidate))

  return result


# Q14