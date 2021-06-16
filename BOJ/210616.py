import collections
import itertools
import math
import sys
input = sys.stdin.readline

# 3460 : 이진수
# t = int(input())
# for i in range(t):
#     num = int(input())
#     bin_num = bin(num)[2:]
#     l = len(bin_num)-1
#     temp = [str(l-idx) for idx,val in enumerate(bin_num) if val == '1']
#     print(' '.join(temp[::-1]))

# 10808 : 최대, 최소
# n = int(input())
# nums = list(map(int,input().split()))
# print(str(min(nums)),str(max(nums)),sep=' ')

# 2460 : 지능형 기차 2
# max_people = 0
# current = 0
# for _ in range(10):
#     people_in, people_out = map(int,input().split())
#     current = current - people_in + people_out
#     max_people = max(max_people, current)
# print(max_people)

# 10870 : 피보나치 수 5
# dp = collections.defaultdict(int)
# dp[0] = 0
# dp[1] = 1
#
# n = int(input())
# if n <= 1:
#     print(dp[n])
# else:
#     for i in range(2,n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     print(dp[n])

# 2309 : 일곱 난쟁이
# smalls = []
# for _ in range(9):
#     smalls.append(int(input()))
# cases = list(itertools.combinations(smalls,7))
# for case in cases:
#     if sum(case) == 100:
#         temp = list(case)
#         temp.sort()
#         print(*temp,sep='\n')
#         break

# 2609 : 최대공약수와 최소공배수
# def gcd(a: int, b: int) -> int:
#     if b == 0:
#         return a
#
#     a, b = b, a % b
#     return gcd(a,b)
#
# def lcm(a: int, b: int) -> int:
#     return int(a * b / gcd(a,b))
#
# a, b = map(int,input().split())
# print(gcd(a,b))
# print(lcm(a,b))

# 2693 : N번째 큰 수
# n = int(input())
# for _ in range(n):
#     temp = list(map(int,input().split()))
#     temp.sort()
#     print(temp[-3])

# 1978 : 소수 찾기
# def prime_range(n):
#   num_array = [False,False] + [True]*(n-1)
#   for i in range(2,int(math.sqrt(n))+1):
#     if num_array[i] == True:
#       for j in range(i*2,n+1,i):
#         num_array[j] = False
#   return num_array
#
# n = int(input())
# prime_list = prime_range(1000)
# nums = map(int,input().split())
# print(sum([prime_list[i] for i in nums]))

# 1292 : 쉽게 푸는 문제
# problems = []
# for i in range(1,46):
#     problems.extend([i]*i)
# start, end = map(int, input().split())
# print(sum(problems[start-1:end]))

# 2581 : 소수
def prime_range(n):
  num_array = [False,False] + [True]*(n-1)
  for i in range(2,int(math.sqrt(n))+1):
    if num_array[i] == True:
      for j in range(i*2,n+1,i):
        num_array[j] = False
  return num_array
prime_list = prime_range(10000)
start, end = int(input()), int(input())
primes = [i for i in range(start,end+1) if prime_list[i]]
if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))