import sys
input = sys.stdin.readline

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