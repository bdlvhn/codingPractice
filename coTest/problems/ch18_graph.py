import sys
input = sys.stdin.readline
from collections import deque

def q41():
  n,m = map(int,input().split())
  temp = []
  for _ in range(n):
    temp.append([*map(int,input().split())])
  travel = [*map(int,input().split())]
  parent = [i for i in range(n+1)]

  def find_parent(parent,x):
    if parent[x]!=x:
      parent[x] = find_parent(parent,parent[x])
    return parent[x]

  def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a>b:
      parent[a] = b
    else:
      parent[b] = a

  for a in range(1,n+1):
    for b in range(1,n+1):
      if temp[a-1][b-1]==1:
        union_parent(parent,a,b)
  
  result = True
  for i in range(m-1):
    if find_parent(parent,travel[i]) != find_parent(parent,travel[i+1]):
      result = False

  return 'YES' if result else 'NO'

# print(q41())

def q42():
  g = int(input())
  p = int(input())
  flights = []
  for _ in range(p):
    flights.append(int(input()))
  
  parent = [i for i in range(g+1)]
  def find_parent(parent,x):
    if parent[x]!=x:
      parent[x] = find_parent(parent,parent[x])
    return parent[x]
  
  def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
      parent[a] = b
    else:
      parent[b] = a

  cnt = 0
  for flight in flights:
    switch = False
    for f in range(flight,0,-1):
      if not switch and (find_parent(parent,0) != find_parent(parent,f)):
        union_parent(parent,0,f)
        switch = True
        cnt += 1
    if not switch:
      return cnt

# print(q42())

def q43():
  n,m = map(int,input().split())
  street_lamp = []
  total_cost = 0
  for _ in range(m):
    a,b,c = map(int,input().split())
    street_lamp.append((c,a,b))
    total_cost += c
  street_lamp.sort()
  parent = [i for i in range(n)]

  def find_parent(parent,x):
    if parent[x]!=x:
      parent[x] = find_parent(parent,parent[x])
    return parent[x]
  
  def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
      parent[a] = b
    else:
      parent[b] = a
  print(street_lamp)

  spend_cost = 0
  for lamp in street_lamp:
    cost, a, b = lamp
    if find_parent(parent,a) != find_parent(parent,b):
      union_parent(parent,a,b)
      spend_cost += cost
  
  print(total_cost-spend_cost)

# q43()

def q44():
  def find_parent(parent,x):
    if parent[x] != x:
      parent[x] = find_parent(parent,parent[x])
    return parent[x]

  def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a>b:
      parent[a] = b
    else:
      parent[b] = a

  n = int(input())
  parent = [i for i in range(n)]
  
  x,y,z = [],[],[]
  for i in range(n):
    data = [*map(int,input().split())]
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))

  x.sort()
  y.sort()
  z.sort()

  edges = []
  for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))
  edges.sort()

  min_cost = 0
  for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
      union_parent(parent,a,b)
      min_cost+=cost

  print(min_cost)

# q44()

def q45():
  test_cases = int(input())
  for _ in range(test_cases):
    n = int(input())
    before_rank = [0] + [*map(int,input().split())]
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for i in range(1,n+1):
      for team in before_rank[i+1:]:
        graph[before_rank[i]].append(team)
        indegree[team]+=1

    def topology_sort():
        result = []
        q = deque()

        for v in range(1,n+1):
          if indegree[v]==0:
            q.append(v)
        
        cycle = False
        plural = False
        for _ in range(n):
          if len(q)==0:
            cycle = True
            break
          elif len(q)>=2:
            plural = False
            break
          now = q.popleft()
          result.append(now)
          for a in graph[now]:
            indegree[a]-=1
            if indegree[a]==0:
              q.append(a)

        return ' '.join(map(str,result)), cycle, plural

    m = int(input())
    change_list = []
    for _ in range(m):
      change_list.append([*map(int,input().split())])
    for change in change_list:
      a,b = change
      if a in graph[b]:
        graph[b].remove(a)
        indegree[a]-=1
        graph[a].append(b)
        indegree[b]+=1
      else:
        graph[a].remove(b)
        indegree[b]-=1
        graph[b].append(a)
        indegree[a]+=1

    result, cycle, plural = topology_sort()
    if cycle:
      print('IMPOSSIBLE')
    elif plural:
      print('?')
    else:
      print(result)

q45()