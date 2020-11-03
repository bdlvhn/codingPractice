"""JasenCase 문자열 만들기"""
def solution(s):
    isWord = 0
    ans = []
    for word in s:
        if word == ' ':
            isWord = 0
            ans.append(word)
        elif word.isalpha():
            if isWord == 0:
                ans.append(word.upper())
                isWord += 1
            else:
                ans.append(word.lower())
                isWord += 1
        else:
            ans.append(word)
            isWord += 1
    return ''.join(ans)


"""피보나치 수"""
from functools import reduce

def solution(n):
    l = [0,1]
    for i in range(n-1):
        l.append(l[-1]+l[-2])
    return l[-1]%1234567


"""최솟값 만들기"""
def solution(A,B):
    A, B = A.sort(), B.sort()
    ans = 0

    for i in range(len(A)):
        if A[0]*B[-1] >= A[-1]*B[0]:
            ans += A.pop(0)*B.pop(-1)
        else:
            ans += A.pop(-1)*B.pop(0)
    return ans


"""가장 큰 정사각형 찾기"""
from itertools import chain
def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1]) + 1
                
    return max(list(chain(*board)))**2


"""최댓값과 최솟값"""
def solution(s):
    l = list(map(int,s.split(' ')))
    return ''.join([str(min(l)),' ',str(max(l))])


"""올바른 괄호"""
def solution(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt +=1
        else:
            cnt -=1
        if cnt<0:
            return False
    return True if cnt == 0 else False

