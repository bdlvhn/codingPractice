### 7,순차 탐색 예제, time complexity : O(N)
def sequential_search(n,target,array):
  for i in range(n):
    if array[i] == target:
      return i + 1

### 7,이진 탐색 재귀 함수,  time complexity : O(NlogN)
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

### 7,이진 탐색 반복 함수,  time complexity : O(NlogN)
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
import sys
input_data = sys.stdin.readline().rstrip()



### 7,2 부품 찾기
n = int(input())
store = list(map(int,input().split()))
m = int(input())
client = list(map(int,input().split()))

### 7,2 부품 찾기, 이진 탐색
store.sort()
for elm in client:
  if binary_search(store,elm,0,n-1) != None:
    print("yes",end=" ")
  else:
    print("no",end=" ")

### 7,2 부품 찾기, 계수 정렬
array = [0] * 1000001

for x in store:
  array[x] = 1

for y in client:
  if array[y] == 1:
    print('yes',end=' ')
  else:
    print('no',end=' ')

### 7,2 부품 찾기, 집합 자료형
for x in client:
  if x in store:
    print('yes',end=' ')
  else:
    print('no',end=' ')



### 7,2 떡볶이 떡 만들기
n, m = map(int,input().split())
riceCake = list(map(int,input().split()))
riceCake.sort()

def h_cut(array,target,start,end):
  print(array,target,start,end)
  if start>end:
    return None

  h = (start+end)//2
  left = sum(map(lambda x: x-h if x>h else 0, array))
  print(target,left)
  if target == left:
    return h
  elif target < left:
    return h_cut(array,target,h+1,end)
  elif target > left:
    return h_cut(array,target,start,h-1)

print(h_cut(riceCake,m,0,riceCake[n-1]))

### 반복 탐색
def h_cut_02(array,target,start,end):
  result = 0
  while (start<=end):
    total = 0
    h = (start+end)//2
    for x in array:
      if x > h:
        total += x - min
    
    if total < target:
      end = h - 1
    else:
      result = h
      start = h + 1

  return result
