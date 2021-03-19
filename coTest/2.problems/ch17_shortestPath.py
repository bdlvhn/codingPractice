import sys
input = sys.stdin.readline
import heapq
def q37():
  INF = 1e9
  n = int(input())
  m = int(input())
  table = [[INF]*(n+1) for _ in range(n+1)]
  for i in range(1,n+1):
    table[i][i] = 0
  for _ in range(m):
    x,y,c = map(int,input().split())
    table[x][y] = min(table[x][y],c)
  
  for k in range(1,n+1):
    for a in range(1,n+1):
      for b in range(1,n+1):
        table[a][b] = min(table[a][b],table[a][k]+table[k][b])
  
  for x in range(1,n+1):
    for y in range(1,n+1):
      if table[x][y]==INF:
        table[x][y]=0
  
  for row in table[1:]:
    print(' '.join(map(str,row[1:])))

# q37()

def q38():
  INF = 9
  n, m = map(int,input().split())
  table = [[INF]*(n+1) for _ in range(n+1)]
  for i in range(1,n+1):
    table[i][i] = INF
  for _ in range(m):
    a,b = map(int,input().split())
    table[a][b] = 1
  
  for k in range(1,n+1):
    for a in range(1,n+1):
      for b in range(1,n+1):
        if min(table[a][b],table[a][k]+table[k][b]) < INF:
          table[a][b] = 1

  for i in range(1,n+1):
    for j in range(1,n+1):
      if table[i][j]==INF:
        table[i][j] = 0
  
  table = [row[1:] for row in table[1:]]
  answer = 0

  for i in range(n):
    if sum(table[i]) + sum(map(lambda x:x[i],table)) == n-1:
      answer+=1
  print(answer)

# q38()

def q39():
  def dijkstra(x,y):
    INF = 1e9
    distance = [[INF]*n for _ in range(n)]
    distance[x][y] = board[x][y]
    q = []
    heapq.heappush(q,(distance[x][y],[x,y]))
    while q:
      dist, now = heapq.heappop(q)
      if distance[now[0]][now[1]] < dist:
        continue
      dx,dy = [1,0,-1,0],[0,1,0,-1]
      for d in range(4):
        nx,ny = now[0]+dx[d],now[1]+dy[d]
        # print('nx,ny :',nx,ny)
        if nx>=0 and nx<n and ny>=0 and ny<n:
          cost = dist + board[nx][ny]
          # print('cost :',cost)
          if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q,(cost,[nx,ny]))
    return distance
  
  t = int(input())
  for _ in range(t):
    n = int(input())
    board = [[]*n for _ in range(n)]
    for i in range(n):
      board[i] = [*map(int,input().split())]
    print(dijkstra(0,0)[n-1][n-1])

# q39()

def q40():
  n, m = map(int,input().split())
  graph = [[]*(n+1) for _ in range(n+1)]
  for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
  
  print(*graph,sep="\n")
  
  def dijkstra(start):
    INF = 1e9
    distance = [INF]*(n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
      dist, now = heapq.heappop(q)
      print('q:',q)
      print('dist,now:',dist,now)
      if distance[now] < dist:
        continue
      for nxt in graph[now]:
        cost = dist + nxt[1]
        print('cost:',cost)
        if distance[nxt[0]] > cost:
          distance[nxt[0]] = cost
          heapq.heappush(q,(cost,nxt[0]))
    return distance
  
  
  distance = dijkstra(1)[1:]
  resB = max(distance)
  resA = distance.index(resB)+1
  resC = distance.count(resB)
  print(resA, resB, resC,sep=" ")

# q40()