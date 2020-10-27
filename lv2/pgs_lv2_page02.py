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


