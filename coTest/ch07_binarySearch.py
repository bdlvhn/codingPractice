import sys
input = sys.stdin.readline

### 7, 순차 탐색, time complexity : O(N)
def sequential_search(n,target,array):
  for i in range(n):
    if array[i] == target:
      return i + 1

### 7, 이진 탐색 재귀 함수, time complexity : O(NlogN)
def binary_search(array,target,start,end):
  if start>end:
    return None
  mid = (start+end)//2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array,target,start,mid-1)
  elif array[mid] < target:
    return binary_search(array,target,mid+1,end)

### 7, 이진 탐색 반복 함수, time complexity : O(NlogN)
def binary_search_02(array,target,start,end):
  while start<=end:
    mid = (start+end)//2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    end = mid - 1
  elif array[mid] < target:
    start = mid + 1
  return None

#*# 한 줄 입력받아 출력하는 소스코드

def ch07_q02_01():
  n = int(input())
  nums = [*map(int,input().split())]
  m = int(input())
  checks = [*map(int,input().split())]
  nums.sort()

  def binary_search(array,target,start,end):
    if start > end:
      return "no"
    mid = (start+end)//2
    if target == array[mid]:
      return "yes"
    elif target < array[mid]:
      return binary_search(array,target,start,mid-1)
    else:
      return binary_search(array,target,mid+1,end)
  
  for check in checks:
    print(binary_search(nums,check,0,n-1),end=' ')
  
# ch07_q02_01()

def ch07_q02_02():
  n = int(input())
  nums = [*map(int,input().split())]
  m = int(input())
  checks = [*map(int,input().split())]

  numArray = [0]*(max(nums)+1)
  for i in nums:
    numArray[i] += 1
  for j in checks:
    if numArray[j]:
      print('yes',end=' ')
    else:
      print('no',end=' ')

# ch07_q02_02()

def ch07_q02_03():
  n = int(input())
  nums = set(map(int,input().split()))
  m = int(input())
  checks = [*map(int,input().split())]

  for j in checks:
    if j in nums:
      print('yes',end=' ')
    else:
      print('no',end=' ')

# ch07_q02_03()

def ch07_q03():
  n,m = map(int,input().split())
  rices = [*map(int,input().split())]
  rices.sort()

  def rice_cut(l):
    return sum(map(lambda x: (x-l) if (x-l)>0 else 0,rices))

  def binary_search(target,start,end):
    if start > end:
      return None
    mid = (start+end)//2
    mid_cut = rice_cut(mid)
    if target == mid_cut:
      return mid
    elif target < mid_cut:
      return binary_search(target,mid+1,end)
    else:
      return binary_search(target,start,mid-1)
  
  print(binary_search(m,0,max(rices)))

# ch07_q03()