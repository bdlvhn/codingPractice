import sys
input = sys.stdin.readline

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

