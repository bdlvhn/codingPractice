import sys
input = sys.stdin.readline

### 10, 기본적인 서로소 집합 알고리즘

def find_parent(parent,x):
  if parent[x]!=x:
    return find_parent(parent,parent[x])
  return x
# 개선 이전

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]
# 경로 압축 기법으로 개선

def union_parent(parent,a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int,input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
  parent[i] = i

for i in range(e):
  a,b = map(int,input().split())
  union_parent(parent,a,b)

print('각 원소가 속한 집합: ',end='')
for i in range(1,v+1):
  print(find_parent(parent,i),end=' ')
print()

print('부모 테이블: ',end='')
for i in range(1,v+1):
  print(parent[i],end=' ')


### 10, 서로소 집합을 활용한 무방향 사이클 판별
def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int,input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
  parent[i] = i

cycle = False

for i in range(e):
  a,b = map(int,input().split())
  if find_parent(parent,a) == find_parent(parent,b):
    cycle = True
    break
  else:
    union_parent(parent,a,b)

if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지 않았습니다.")


### 10,신장 트리; 크루스칼 알고리즘 ~ 시간복잡도 : O(Elog(E))

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int,input().split())
parent = [0]*(v+1)

edges = []
result = 0

for i in range(1,v+1):
  parent[i] = i

for _ in range(e):
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

for edge in edges:
  cost,a,b = edge
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost

print(result)


### 10, 위상 정렬 ~ 시간복잡도 : O(V+E)

from collections import deque
v,e = map(int,input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
  a,b = map(int,input().split())
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()

  for i in range(1,v+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end=' ')

topology_sort()

def ch10_q02():
  n,m = map(int,input().split())
  teams = [i for i in range(n+1)]

  def find_team(teams,x):
    if teams[x]!=x:
      teams[x] = find_team(teams,teams[x])
    return x
  
  def union_team(teams,a,b):
    a = find_team(teams,a)
    b = find_team(teams,b)
    if a < b:
      teams[b] = a
    else:
      teams[a] = b

  result = []  
  for _ in range(m):
    k,x,y = map(int,input().split())
    if k == 0:
      union_team(teams,x,y)
    else:
      a,b = find_team(teams,x), find_team(teams,y)
      if a==b:
        result.append('YES')
      else:
        result.append('NO')
  
  for r in result:
    print(r)

# ch10_q02()
  
def ch10_q03():
  n,m = map(int,input().split())
  parent = [i for i in range(n+1)]
  edges = []
  for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
  edges.sort()

  def find_parent(parent,x):
    if parent[x]!=x:
      parent[x] = find_parent(parent,parent[x])
    return parent[x]

  def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
      parent[b] = a
    else:
      parent[a] = b

  max_cost = 0
  total_cost = 0
  for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
      union_parent(parent,a,b)
      max_cost = cost
      total_cost += cost

  print(total_cost - max_cost)

# ch10_q03()

from collections import deque
import copy

def ch10_q04():
  n = int(input())
  lectures = [0]*(n+1)
  graph = [[] for i in range(n+1)]
  indegree = [0]*(n+1)

  for i in range(1,n+1):
    temp = [*map(int,input().split())]
    lectures[i] = temp[0]
    for t in temp[1:-1]:
      graph[t].append(i)
      indegree[i] += 1

  def topology_sort():
    times = copy.deepcopy(lectures)
    q = deque()
    for i in range(1,n+1):
      if indegree[i] == 0:
        q.append(i)

    while q:
      now = q.popleft()
      for i in graph[now]:
        times[i] = max(times[i],times[now]+lectures[i])
        indegree[i] -= 1
        if indegree[i] == 0:
          q.append(i)
      
    return times
    
  times = topology_sort()

  for i in range(1,n+1):
    print(times[i])

ch10_q04()