import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def q27():
  n,x = map(int,input().split())
  numList = [*map(int,input().split())]
  numList.sort()
  l, r = bisect_left(numList,x), bisect_right(numList,x)
  return len(numList[l:r]) if numList[l:r] else -1

# print(q27())

def q28():
  n = int(input())
  array = [*map(int,input().split())]

  def binary_search(array,start,end):
    if start > end:
      return None
    mid = (start + end)//2

    if array[mid] == mid:
      return mid
    elif array[mid] > mid:
      return binary_search(array,start,mid-1)
    elif array[mid] < mid:
      return binary_search(array,mid+1,end)
  
  idx = binary_search(array,0,n-1)

  if idx==None:
    print(-1)
  else:
    print(idx)

q28()
