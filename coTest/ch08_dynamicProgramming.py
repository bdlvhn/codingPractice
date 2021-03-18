import sys
input = sys.stdin.readline

### 8,피보나치 코드, 재귀함수 반복계산 (효율성 떨어짐)
# def fibo(x):
#   if x==1 or x==2:
#     return 1
#   return fibo(x-1) + fibo(x-2)

### 8,피보나치 코드, 탑다운
d = [0] * 101

def fibo_td(x):
  if x==1 or x==2:
    return 1

  if d[x]!=0:
    return d[x]
  
  d[x] = fibo_td(x-1) + fibo_td(x-2)
  return d[x]

### 8,피보나치 코드, 바텀업
d = [0] * 101

def fibo_bu(x):
  d[1], d[2] = 1, 1
  n = 100

  for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

  return d[n]
  
def ch08_q02():
  x = int(input())
  d = [0] * 30001
  for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i%2==0:
      d[i] = min(d[i], d[i//2] + 1)
    if i%3==0:
      d[i] = min(d[i], d[i//3] + 1)
    if i%5==0:
      d[i] = min(d[i], d[i//5] + 1)

  return d[x]

# print(ch08_q02())

def ch08_q03():
  n = int(input())
  wh = [*map(int,input().split())]
  d = [0] * 100
  d[0] = wh[0]
  d[1] = max(wh[0],wh[1])
  for i in range(2,n):
    d[i] = max(wh[i]+d[i-2],d[i-1])
  
  return max(d)

# print(ch08_q03())

def ch08_q04():
  n = int(input())
  d = [0]*(1000+1)
  d[1] = 1
  d[2] = 3

  for i in range(3,n+1):
    d[i] = (d[i-1] + 2*d[i-2])
  return d[n] % 796796

# print(ch08_q04())
  
def ch08_q05():
  n,m = map(int,input().split())
  coins = []
  for _ in range(n):
    coins.append(int(input()))

  d = [0]*10001
  for coin in coins:
    d[coin] = 1
  for i in range(1,m+1):
    for coin in coins:
      if i-coin > 0:
        if d[i-coin] and d[i]==0:
          d[i] = d[i-coin]+1
        else:
          d[i] = min(d[i-coin]+1,d[i])
  print(d)
  return d[m] if d[m] else -1

print(ch08_q05())