import time
from collections import deque

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

### DFS 예제 - 스택 기반
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

visited = [False] * 9

dfs(graph, 1, visited)



### BFS 예제 - 큐 기반
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited = [False] * 9

print('\n')
bfs(graph, 1, visited)



### Ch05,3: 음료수 얼려 먹기
def solution_03():
  n, m = map(int,input().split())
  graph = []
  for _ in range(n):
    graph.append(list(map(int,input().split())))

  def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
      return False
    
    if graph[x][y]==0:
      graph[x][y]=1  
      dfs(x+1,y)
      dfs(x-1,y)
      dfs(x,y+1)
      dfs(x,y-1)
      return True
    return False

  result = 0
  for i in range(n):
    for j in range(m):
      if dfs(i,j) == True:
        result += 1
  
  return result

# print(solution_03())



### Ch05,4: 미로 탈출
n, m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny]==0:
        continue
      
      if graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))

  return graph[n-1][m-1]

print(bfs(0,0))
