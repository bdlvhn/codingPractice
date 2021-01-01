### 8,피보나치 코드, 재귀함수 반복계산으로 효율성 떨어짐
# def fibo(x):
#   if x==1 or x==2:
#     return 1
#   return fibo(x-1) + fibo(x-2)

### 8,피보나치 코드, 탑다운
# d = [0] * 101

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

### 8,2 1로 만들기
# d = [0] * 30001
  
def make_one(x):
  d[1] = 0

  for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i%2==0:
      d[i] = min(d[i], d[i//2] + 1)
    if i%3==0:
      d[i] = min(d[i], d[i//3] + 1)
    if i%5==0:
      d[i] = min(d[i], d[i//5] + 1)

  return d[x]

# i = int(input())
# print(make_one(i))



### 8,3 개미 전사
# i = int(input())
# store = [0] + list(map(int,input().split()))
# d = [0] * len(store)

def ant_fighter(i,store,d):
  d[1] = store[1]
  d[2] = max(store[1],store[2])
  for i in range(3,len(store)):
    d[i] = max(d[i-2]+store[i],d[i-1])
  
  return d[i]

# print(ant_fighter(i,store,d))

### 8,4 바닥 공사
# i = int(input())
# d = [0]*(1000+1)
# d[1] = 1
# d[2] = 3

def floor_cnst(x,d):
  for i in range(3,len(d)):
    d[i] = (d[i-1] + 2 * d[i-2])%796796

  return d[x]

# print(floor_cnst(i,d))



### 8,5 효율적인 화폐 구성
n, m = map(int,input().split())
array = []
for _ in range(n):
  array.append(int(input()))

d = [0] + [9999] * (10000)

def coin_combi(n,m,array,d):
  for i in range(n):
    for j in range(array[i],m+1):
      d[j] = min(d[j],d[j-array[i]]+1)

  return d[j] if d[j]!=9999 else -1

print(coin_combi(n,m,array,d))
