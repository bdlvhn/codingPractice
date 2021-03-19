def ch03_q02():
  n,m,k = map(int,input().split())
  num_list = [*map(int,input().split())]

  num_list.sort(reverse=True)
  a,b = num_list[:2]
  ans_list = [a]*k + [b]
  ans_len = len(ans_list)
  return sum(ans_list*(m//ans_len) + ans_list[:(m%ans_len)])

# print(ch03_q02())

def ch03_q03():
  n,m = map(int,input().split(" "))
  num_list = []
  for _ in range(n):
    num_list.append([*map(int,input().split())])
  return max(map(min,num_list))

# print(ch03_q03())

def ch03_q04():
  n,k = map(int,input().split(" "))
  cnt = 0

  while n!=1:
    if (n%k==0):
      n /= k
      cnt += 1
    else:
      n -= 1
      cnt += 1
  
  return cnt