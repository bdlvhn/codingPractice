### 10,예제 - 기본적인 서로소 집합 알고리즘

# def find_parent(parent,x):
#   if parent[x]!=x:
#     return find_parent(parent,parent[x])
#   return x
# 개선 이전

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]
# # 경로 압축 기법으로 개선

def union_parent(parent,a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int,input().split())
parent = [0] * (v + 1)

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


### 10,예제 - 서로소 집합을 활용한 사이클 판별
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
parent = [0] * (v + 1)

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


### 10,예제 - 신장 트리 / 크루스칼 알고리즘 ~ O(Elog(E))

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
parent = [0] * (v + 1)

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


### 10,예제 - 위상 정렬 ~ O(V+E)
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


### 10,2 팀 결성
def find_team(team,x):
  if team[x]!=x:
    team[x] = find_team(team,team[x])
  return team[x]

def union_team(team,a,b):
  a = find_team(team, a)
  b = find_team(team, b)
  if a < b:
    team[b] = a
  else:
    team[a] = b

n,m = map(int,input().split())
team = [0] * (n + 1)
answer = []

for i in range(n):
  team[i] = i

for _ in range(m):
  x,a,b = map(int,input().split())
  if x==0:
    union_team(team,a,b)
  elif x==1:
    if find_team(team,a) == find_team(team,b):
      answer.append("YES")
    else:
      answer.append("NO")

for ans in answer:
  print(ans)


### 10,3 도시 분할 계획
def find_town(town,x):
  if town[x]!=x:
    town[x] = find_town(town,town[x])
  return town[x]

def union_town(town,a,b):
  a = find_town(town,a)
  b = find_town(town,b)
  if a<b:
    town[b] = a
  else:
    town[a] = b

n,m = map(int,input().split())
town = [0] * (n+1)

for i in range(n+1):
  town[i] = i

roads = []
result = 0

for _ in range(m):
  a,b,cost = map(int,input().split())
  roads.append((cost,a,b))

roads.sort()
last = 0

for road in roads:
  cost,a,b = road
  if find_town(town,a) != find_town(town,b):
    union_town(town,a,b)
    result += cost
    last = cost

print(result - last)


### 10,4 커리큘럼
from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1,v+1):
  data = list(map(int,input().split()))
  time[i] = data[0]
  for x in data[1:-1]:
    indegree[i] += 1
    graph[x].append(i)

def topology_sort():
  result = copy.deepcopy(time)
  q = deque()

  for i in range(1,v+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    for i in graph[now]:
      result[i] = max(result[i],result[now]+time[i])
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in range(1,v+1):
    print(result[i])

topology_sort()
