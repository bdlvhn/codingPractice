import sys
import math
from itertools import combinations
input = sys.stdin.readline



# 소수 찾기
def is_prime_number(x):
  for i in range(2,int(math.sqrt(x))+1):
    if x % i == 0:
      return True
  return False

# 소수 범위 찾기
# 시간 복잡도 : O(NloglogN); 빠르지만 많은 메모리
def prime_range(n):
  num_array = [False,False] + [True]*(n-1)
  for i in range(2,int(math.sqrt(n))+1):
    if num_array[i] == True:
      for j in range(i*2,n+1,i):
        num_array[j] = False
  return num_array

# 투 포인터
# e.g. (특정한 합을 가지는 연속 수열 찾기)
n,m,data = 5,5,[1,2,3,2,5] # 데이터 개수, 부분합, 전체 수열
def interval_sum(n,m,data):
  count = 0
  interval_sum = 0
  end = 0

  for start in range(n):
    while interval_sum < m and end < n:
      interval_sum += data[end]
      end += 1

    if interval_sum == m:
      count += 1
    interval_sum -= data[start]

# e.g. (정렬되어 있는 두 리스트의 합집합)
# 시간복잡도 : O(N+M)
a,b = [1,3,5],[2,4,6,8]
def union_two_sorted_list(a,b):
  n,m = len(a),len(b)
  i=j=0
  result = []

  while i<n or j<m:
    if j>=m or (i<n and a[i]<=b[j]):
      result.append(a[i])
      i+=1
    else:
      result.append(b[j])
      j+=1
  print(' '.join(map(str,result)))
# print(union_two_sorted_list(a,b))

# 구간 합 계산
n,data = 5,[10,20,30,40,50]
def partial_sum(left,right):
  sum_value = 0
  prefix_sum = [0]
  for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
  
  return prefix_sum[right]-prefix_sum[left-1]

def q_b1(m,n):
  num_array = [False,False] + [True]*(n-1)
  for i in range(2,int(math.sqrt(n))+1):
    if num_array[i] == True:
      for j in range(i*2,n+1,i):
        num_array[j] = False
  result = [idx for idx,val in enumerate(num_array) if idx>=m and val]
  print(*result,sep="\n")

m,n = map(int,input().split())
q_b1(m,n)

def q_b2():
  l,c = map(int,input().split())
  word_list = [*map(str,input().split())]
  word_list.sort()

  word_sets = [*map(''.join,[*combinations(word_list,l)])]
  vowels = ['a','e','i','o','u']
  for word in word_sets:
    cnt = [0,0]
    for w in word:
      if w in vowels:
        cnt[0] += 1
      else:
        cnt[1] += 1
    if cnt[0]>=1 and cnt[1]>=2:
      print(word)

q_b2()