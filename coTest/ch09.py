import sys
input = sys.stdin.readline
INF = int(1e9)


### 9,예제 - 간단한 Dijkstra 알고리즘
n,m = map(int,input().split()) # 노드, 간선 갯수
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True

  for j in graph[start]:
    distance[j[0]] = j[1]
  
  for i in range(n-1):
    now = get_smallest_node()
    visited[now] = True
  
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])


### 9,예제 - 개선된 Dijkstra 알고리즘
import heapq

n,m = map(int,input().split()) # 노드, 간선 갯수
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])


### 9,예제 - 플로이드 워셜 알고리즘
n,m = map(int,input().split()) # 노드, 간선 갯수
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  graph[i][i] = 0

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a][b] = c

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b] == INF:
      print("INFINITY", end=" ")
    else:
      print(graph[a][b], end=" ")
  print()


### 9,2 미래도시
INF = int(1e9)

def q09_2():
  n,m = map(int,input().split())
  graph = [[INF]*(n+1) for _ in range(n+1)]

  for i in range(1,n+1):
    graph[i][i] = 0

  for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

  x,k = map(int,input().split())

  for k in range(1,n+1):
    for a in range(1,n+1):
      for b in range(1,n+1):
        graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

  for a in graph:
    print(a)
  
  return graph[1][k] + graph[k][x] if (graph[1][k] + graph[k][x] < INF) else -1

# print(q09_2())


### 9,3 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(c)
print(graph,distance)


count = 0
max_distance = 0
for d in distance:
  if d != INF:
    count += 1
    max_distance = max(max_distance,d)

print(count-1,max_distance)
