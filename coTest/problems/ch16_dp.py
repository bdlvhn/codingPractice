import sys
input = sys.stdin.readline


def q31():
    def transform_list(temp, n, m):
        return [temp[m * i:m * (i + 1)] for i in range(n)]

    def mine_gold(n, m):
        trace = [[0] * (m + 2) for _ in range(n + 2)]

        for i in range(n):
            trace[i + 1][1] = mine[i][0]

        for j in range(1, m):  # 모든 열
            for i in range(n):  # 모든 행
                trace[i + 1][j + 1] = mine[i][j] + max(
                    trace[i][j], trace[i + 1][j], trace[i + 2][j])
        print(max(map(lambda x: x[-2], trace)))

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        temp = [*map(int, input().split())]
        mine = transform_list(temp, n, m)
        print(n, m)
        print(*mine, sep="\n")
        mine_gold(n, m)


# q31()


def q32():
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append([*map(int, input().split())])

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                left_value = 0
            else:
                left_value = triangle[i - 1][j - 1]
            if j == i:
                right_value = 0
            else:
                right_value = triangle[i - 1][j]
            triangle[i][j] = triangle[i][j] + max(left_value, right_value)

    print(max(triangle[-1]))


# q32()


def q33():
    n = int(input())
    counsels = [[0, 0]]
    for _ in range(n):
        counsels.append([*map(int, input().split())])

    answer = [[0] for _ in range(n + 2)]
    for d in range(1, n + 1):
        answer[d].append(max(answer[d - 1]))
        if d + (counsels[d][0]) <= n + 1:
            answer[(d +
                    (counsels[d][0]))].append(max(answer[d]) + counsels[d][1])
    print(max([*map(max, answer)]))


# q33()

def q34():
    n = int(input())
    num_list = [*map(int, input().split())]
    num_list.reverse()
    len_list = [1]*n

    for i in range(1,n):
      for j in range(i):
        if num_list[j] < num_list[i]:
          len_list[i] = max(len_list[i],len_list[j]+1)

    return n - max(len_list)

# print(q34())

def q35():
  n = int(input())

  ugly = [0] * n
  ugly[0] = 1

  i2 = i3 = i5 = 0
  next2, next3, next5 = 2, 3, 5

  for l in range(1, n):
      ugly[l] = min(next2, next3, next5)
      if ugly[l] == next2:
          i2 += 1
          next2 = ugly[i2] * 2
      if ugly[l] == next3:
          i3 += 1
          next3 = ugly[i3] * 3
      if ugly[l] == next5:
          i5 += 1
          next5 = ugly[i5] * 5
  print(ugly[n - 1])


import sys
input = sys.stdin.readline
def q36():
  def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]

  str1 = input()
  str2 = input()

  print(edit_dist(str1, str2))