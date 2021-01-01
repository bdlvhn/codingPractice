array = [7,5,9,0,3,1,6,2,4,8]

### 6,선택 정렬 예제, time complexity : O(N^2)

def sort_selection(array):
  for i in range(len(array)):
    min_idx = i
    for j in range(1,i):
      if array[min_idx]>array[j]:
        min_idx = j
    array[i],array[min_idx] = array[min_idx],array[i]\

# sort_selection(array)
# print(array)

### 6,삽입 정렬 예제, time complexity : O(N^2)

def sort_insert(array):
  for i in range(1,len(array)):
    for j in range(i,0,-1):
      if array[j] < array[j-1]:
        array[j], array[j-1] = array[j-1], array[j]
      else:
        break
  
  return array

# sort_insert(array)
# print(array)

### 6,퀵 정렬 예제, time complexity : O(NlogN)

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

# sort_quick(array, 0, len(array)-1)
# print(array)

### 6,퀵 정렬 예제 2, time complexity : O(NlogN)

def quick_sort(array):

  if len(array)<=1:
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))

### 6, 계수 정렬 예제, time complexity : O(N+K)

# array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#   count[array[i]] += 1

# for i in range(len(count)):
#   for j in range(count[i]):
#     print(i, end = ' ')



### 6,2 위에서 아래로

# n = int(input())
# array = []
# for _ in range(n):
#   array.append(int(input()))

def qck_srt(array):
  if len(array) <= 1:
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x > pivot]
  right_side = [x for x in tail if x <= pivot]

  return qck_srt(left_side) + [pivot] + qck_srt(right_side)

# print(qck_srt(array))



### 6,3 성적이 낮은 순서로 학생 출력하기
# n = int(input())
# array = []
# for _ in range(n):
#   a,b = input().split()
#   array.append((a,int(b)))

# def sort_student(array):
#   return ' '.join(list(map(lambda x:x[0],sorted(array,key = lambda x : x[1]))))

# print(sort_student(array))



### 6,4 두 배열의 원소 교체
n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
  else:
    break

print(sum(A))
