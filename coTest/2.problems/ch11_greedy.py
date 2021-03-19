# Ch11, 그리디 문제

# Q1 : 모험가 길드
def ch11_q01():
  n = int(input())
  members = list(map(int,input().split()))
  cnt = 1

  for i in range(2,n+1):
    if members.cnt(i) >= i:
      cnt += 1
  return cnt

# print(ch11_q01())

# Q2 : 곱하기 혹은 더하기
def ch11_q02():
  s = [int(i) for i in input()]
  ans = s[0]
  
  for i in range(1,len(s)):
    if (ans+s[i]) > (ans*s[i]):
      ans += s[i]
    else:
      ans *= s[i]
  
  return ans

# print(ch11_q02())

# Q3 : 문자열 뒤집기
def ch11_q03():
  s = [i for i in input()]
  cnt = 0
  print(s)
  for j in range(len(s)-1):
    if s[j] != s[j+1]:
      cnt += 1
  
  return cnt-1

# print(ch11_q03())

# Q4 : 만들 수 없는 금액
def ch11_q04():
  n = int(input())
  coins = list(map(int,input().split()))
  coins.sort()
  target = 1

  for coin in coins:
    if coin==1:
      target += 1
    elif target >= coin:
      target += coin
    else:
      return target
  
  return target

# print(ch11_q04())

# Q05 : 볼링공 고르기
from itertools import combinations
def ch11_q05():
  n,m = map(int,input().split())
  weight = list(map(int,input().split()))
  
  return len([i for i in combinations(weight,2) if i[0] != i[1]])

# print(ch11_q05())

# Q06 : 무지의 먹방 라이브





### answer code on the book
# Q1 : 모험가 길드
def ch11_q01b():
  n = int(input())
  data = list(map(int,input().split()))
  data.sort()
  group, count = 0

  for i in data:
    count += 1
    if count>=i:
      group += 1
      count = 0
  return group

# Q2 : 곱하기 혹은 더하기
def ch11_q02b():
  data = input()
  result = int(data[0])

  for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
      result += num
    else:
      result *= num
  
  return result

# Q3 : 문자열 뒤집기
def ch11_q03b():
  data = input()
  count0 = 0
  count1 = 0

  if data[0]=='1':
    count0 += 1
  else:
    count1 += 1
  
  for i in range(len(data)-1):
    if data[i] != data[i+1]:
      if data[i+1]=='1':
        count0 += 1
      else:
        count1 += 1

  return min(count0,count1)

# Q4 : 만들 수 없는 금액
def ch11_q04():
  n = int(input())
  data = list(map(int,input().split()))
  data.sort()
  target = 1

  for x in data:
    if target < x:
      break
    target += x
  
  return target

  # Q05 : 볼링공 고르기
def ch11_q05():
  n,m = map(int,input().split())
  data = list(map(int,input().split()))

  array = [0] * 11
  for x in data:
    array[x] += 1
  
  result = 0
  for i in range(1,m+1):
    n -= array[i]
    result += array[i] * n

  return result

# Q06 : 무지의 먹방 라이브
import heapq
def ch11_06(food_times,k):
  if sum(food_times)<=k:
    return -1

  q = []
  for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))
  
  sum_value = 0
  previous = 0
  length = len(food_times)

  while sum_value + ((q[0][0]-previous)*length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous) * length
    length -= 1
    previous = now
  
  result = sorted(q, key=lambda x:x[1])
  return result[(k-sum_value)%length][1]

print(ch11_06([3,1,2],5))