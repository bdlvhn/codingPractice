### 선택 정렬, time complexity : O(N^2)

def sort_selection(array):
  for i in range(len(array)):
    min_idx = i
    for j in range(1,i):
      if array[min_idx]>array[j]:
        min_idx = j
    array[i],array[min_idx] = array[min_idx],array[i]

### 삽입 정렬, time complexity : O(N^2)

def sort_insert(array):
  for i in range(1,len(array)):
    for j in range(i,0,-1):
      if array[j] < array[j-1]:
        array[j], array[j-1] = array[j-1], array[j]
      else:
        break
  
  return array

### 퀵 정렬, time complexity : O(NlogN)

def sort_quick(array,start,end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  sort_quick(array, start, right-1)
  sort_quick(array, right+1, end)

### 6,퀵 정렬 - 2, time complexity : O(NlogN)

def quick_sort(array):

  if len(array)<=1:
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

### 6, 계수 정렬, time complexity : O(N+K)

def count_sort(array):
  count = [0] * (max(array) + 1)

  for i in range(len(array)):
    count[array[i]] += 1

  for i in range(len(count)):
    for j in range(count[i]):
      print(i, end = ' ')

def ch06_q02():
  n = int(input())
  array = []
  for _ in range(n):
    array.append(int(input()))

  array.sort(reverse=True)
  return ' '.join(map(str,array))

# print(ch06_q02())

def ch06_q03():
  n = int(input())
  array = []
  for _ in range(n):
    array.append(input().split())
  
  return ' '.join([*map(lambda x:x[0],sorted(array,key=lambda x:x[1]))])

# print(ch06_q03())

def ch06_q04():
  n,k = map(int,input().split())
  listA = [*map(int,input().split())]
  listB = [*map(int,input().split())]
  listA.sort()
  listB.sort(reverse=True)
  for i in range(k):
    if listA[i]<listB[i]:
      listA[i], listB[i] = listB[i], listA[i]
    else:
      break
  return sum(listA)

print(ch06_q04())
