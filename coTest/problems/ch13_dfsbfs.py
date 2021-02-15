import time


# Q15 : 특정 거리의 도시 찾기
def q15():
    n, m, k, x = map(int, input().split())
    road = [[] for _ in range(n + 1)]
    dist = [1e9] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        road[a].append(b)

    for i in road[x]:
        dist[i] = min(1, dist[i])

    def departure(d, x):
        for j in road[x]:  # x와 이어진 도시
            if road[j]:
                departure(d + 1, j)
            else:
                dist[j] = min(d + 1, dist[j])

    departure(0, x)

    cnt = 0
    for i, v in enumerate(dist):
        if v == k:
            print(i)
            cnt += 1
    if cnt == 0:
        print(-1)


# q15()

# Q16 : 연구소 (! 시간 초과)
from collections import deque
from itertools import combinations, chain
import copy

start = 0


def q16():
    n, m = map(int, input().split())  # 입력
    global start
    start = time.time()

    board = [[-1] * (m + 2) for _ in range(n + 2)]  # 판 생성
    virus = deque()
    cell = deque()
    answer = 0

    for i in range(n):  # 판 이식
        a = list(map(int, input().split()))
        for j in range(m):
            board[i + 1][j + 1] = a[j]
            if a[j] == 0:
                cell.append([i + 1, j + 1])
            elif a[j] == 2:
                virus.append([i + 1, j + 1])

    cases = combinations(cell, 3)  # 경우의 수 생성
    route = {0: [-1, 0], 1: [1, 0], 2: [0, 1], 3: [0, -1]}

    def spread(board, virus):  # 전염
        this_virus = copy.deepcopy(virus)
        while this_virus:
            v = this_virus.popleft()
            for d in range(4):
                x, y = v[0] + route[d][0], v[1] + route[d][1]
                if board[x][y] == 0:
                    this_virus.append([v[0] + route[d][0], v[1] + route[d][1]])
                    board[x][y] = 2
        return board

    def status(board):  # 상태
        print("------------------")
        print("board : ")
        for row in board:
            print(row)
        print("------------------")

    for case in cases:
        new_board = copy.deepcopy(board)
        for c in case:
            new_board[c[0]][c[1]] = 1  # 벽 설치
        spread_board = spread(new_board, virus)
        res_board = list(chain(*spread_board))
        count = 0
        for i in res_board:
            if i == 0:
                count += 1
        answer = max(count, answer)

    return answer


# print(q16())
# end = time.time()
# print(end-start)

# Q17 : 경쟁적 전염
import copy

start = 0


def q17():
    n, k = map(int, input().split())  # 입력 정보
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    s, x, y = map(int, input().split())
    virus_list = [None] * (k + 1)
    global start
    start = time.time()

    for i in range(n):  # 바이러스 시작점
        for j in range(n):
            if board[i][j] != 0:
                if virus_list[board[i][j]] == None:
                    virus_list[board[i][j]] = [[i, j]]
                else:
                    virus_list[board[i][j]].append([i, j])

    def spread(virus, infl):  # 확산
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = virus[0] + dx[i]
            ny = virus[1] + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = infl
                    virus_list[infl].append([nx, ny])
        virus_list[infl].pop(0)

    cnt = 0

    while cnt < s:  # s초간 반복
        for infl in range(1, k + 1):  # 순서대로
            if virus_list[infl] != None:
                new_list = copy.deepcopy(virus_list[infl])
                for virus in new_list:
                    spread(virus, infl)
        cnt += 1

    for row in board:
        print(row)

    return board[x - 1][y - 1]


# print(q17())
# end = time.time()
# print("spent time : ",(end-start))


# Q18 : 괄호 변환
def q18():
    p = input()
    global start
    start = time.time()

    def balanced(p):  # 균형잡혔는지 여부
        return True if p.count("(") == p.count(")") else False

    def right(p):  # 제대로인지 여부
        stack = 0
        for s in p:
            if s == "(":
                stack += 1
            else:
                stack -= 1
            if stack < 0:
                return False
        return True

    def find_balanced(p):
        for i in range(2, len(p) + 1, 2):
            if balanced(p[:i]):
                return i
        return 0

    def result(p):  # 결과 도출
        if right(p):
            return p

        if p == '':
            return ''

        u = p[:find_balanced(p)]
        v = p[find_balanced(p):]

        if right(u):
            return u + result(v)
        else:
            str1 = '(' + result(v) + ')'
            u = u[1:-1]
            if u:
                return str1 + ''.join(['(' if s == ')' else ')' for s in u])

    return result(p)


# print(q18())
# end = time.time()
# print("spent time : ",(end-start))

# Q19 : 연산자 끼워넣기
import sys

def dfs(numbers,result,opers):
    global max_num
    global min_num
    if not numbers:
        max_num = max(max_num,result)
        min_num = min(min_num,result)
        return

    if opers[0]:
        opers[0] -= 1
        dfs(numbers[1:],result+numbers[0],opers)
        opers[0] += 1
    if opers[1]:
        opers[1] -= 1
        dfs(numbers[1:],result-numbers[0],opers)
        opers[1] += 1
    if opers[2]:
        opers[2] -= 1
        dfs(numbers[1:],result*numbers[0],opers)
        opers[2] += 1
    if opers[3]:
        opers[3] -= 1
        if result>0:
            dfs(numbers[1:],result//numbers[0],opers)
        else:
            dfs(numbers[1:],-1*(-1*result//numbers[0]),opers)
        opers[3] += 1

input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
opers = list(map(int,input().split()))
max_num = -1e9
min_num = 1e9
# dfs(numbers[1:],numbers[0],opers)
# print(max_num)
# print(min_num)

# Q20 : 감시 피하기
import sys
import copy
from itertools import combinations

def q20():
  n = int(input())
  board = []
  for _ in range(n):
    board.append(list(input().split()))

  teachers = []
  blanks = []

  for i in range(n):
    for j in range(n):
      if board[i][j] == 'T':
        teachers.append([i,j])
      elif board[i][j] == 'X':
        blanks.append([i,j])

  obstacles = list(combinations(blanks,3))
  
  def watch(teachers,board):
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    for teacher in teachers:
      for i in range(4):
        t = 1
        while 1:
          nx = teacher[0]+t*dx[i]
          ny = teacher[1]+t*dy[i]
          if nx>=0 and nx<n and ny>=0 and ny<n:
            if board[nx][ny] == 'S':
              return True
            elif board[nx][ny] == 'O':
              break
            else:
              t += 1
          else:
            break
    return False

  answer = False

  for obstacle in obstacles:
    temp = copy.deepcopy(board)
    for obs in obstacle:
      temp[obs[0]][obs[1]] = 'O'
    
    if not watch(teachers,temp):
      answer = True

  if answer:
    return 'YES'
  else:
    return 'NO'

print(q20())

