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
  counsels = [[0,0]]
  for _ in range(n):
    counsels.append([*map(int,input().split())])

  answer = [[0] for _ in range(n+2)]
  for d in range(1,n+1):
    answer[d].append(max(answer[d-1]))
    if d+(counsels[d][0]) <= n+1:
        answer[(d+(counsels[d][0]))].append(max(answer[d])+counsels[d][1])
  print(max([*map(max,answer)]))

q33()