import time

### Ch03,2: 큰 수의 법칙
def solution_02():
  n,m,k = map(int,input().split())
  num_list = list(map(int,input().split()))

  # global start_time
  # start_time = time.time()

  num_list.sort(reverse=True)
  a,b = num_list[0], num_list[1]
  # print(a,b)
  ans_list = [a]*k + [b]
  # print(ans_list)
  ans_len = len(ans_list)
  return sum(ans_list*(m//ans_len) + ans_list[:(m%ans_len)])

# print(solution_02())
# end_time = time.time()
# print("time : ", end_time - start_time)



### Ch03,3: 숫자 카드 게임
def solution_03():
  n,m = map(int,input().split(" "))
  num_list = []
  for _ in range(n):
    num_list.append(list(map(int,input().split())))
  
  # global start_time
  # start_time = time.time()
  return max(map(min,num_list))

# print(solution_03())
# end_time = time.time()
# print("time : ", end_time - start_time)



### Ch03,4 : 1이 될 때까지
def solution_04():
  n,k = map(int,input().split(" "))
  cnt = 0

  global start_time
  start_time = time.time()

  while n!=1:
    if (n%k==0):
      n /= k
      cnt += 1
    else:
      n -= 1
      cnt += 1
  
  return cnt

print(solution_04())
end_time = time.time()
print("time : ", end_time - start_time)

