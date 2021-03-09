from collections import deque

def ch05_q03():
  n, m = map(int, input().split())
  graph = []
  for i in range(n):
      graph.append([*map(int, input())])

  def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)
        return True
    else:
        return False

  cnt = 0
  for i in range(n):
      for j in range(m):
          if dfs(i, j):
              cnt += 1

  print(cnt)

# ch05_q03()

def ch05_q04():
  n, m = map(int, input().split())
  graph = []
  for i in range(n):
    graph.append([*map(int, input())])

  dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
  
  def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
      x,y = q.popleft()
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
          if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx,ny))

    print(graph[n-1][m-1])
  
  bfs(0,0)

# ch05_q04()