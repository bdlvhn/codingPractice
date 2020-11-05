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


"""다음 큰 숫자"""
import math
def solution(n):
    a = format(n,'b').count('1')
    for i in range(n+1,2**int(math.log2(n)+2)):
        if a == format(i,'b').count('1'):
            return i
        
        
"""튜플"""
import re

def solution(s):
    p = re.compile('(\d+[,\d]*)')
    l = p.findall(s)
    l = [list(map(int,elm.split(','))) for elm in sorted(l,key=lambda x:len(x))]
    ans = [list(set(l[0]))[0]]
    
    for i in range(len(l)-1):
        ans.append(list(set(l[i+1]) - set(l[i]))[0])
    
    return ans
"""참고 코드
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
"""


"""행렬의 곱셈"""
def solution(arr1, arr2):
    arr2 = [i for i in zip(*arr2)]
    ans = []
    for x1 in arr1:
        w = []
        for x2 in arr2:
            w.append(sum([a*b for a,b in zip(x1,x2)]))
        ans.append(w)
    
    return ans


"""영어 끝말잇기"""
def solution(n, words):
    wordStack = []
    for idx, word in enumerate(words):
        if wordStack:
            if (word not in wordStack) and wordStack[-1][-1] == word[0]:
                wordStack.append(word)
            else:
                return [(idx%n)+1,(idx//n)+1]
        else:
            wordStack.append(word)
    return [0,0]


"""위장"""
from functools import reduce
def solution(clothes):
    dict = {}
    for cloth in clothes:
        if dict.get(cloth[1]):
            dict[cloth[1]] = dict[cloth[1]] + [cloth[0]]
        else:
            dict[cloth[1]] = [cloth[0]]
    return reduce(lambda a,b:a*b,[len(dict[key])+1 for key in dict.keys()]) - 1


"""프린터"""
def solution(priorities, location):
    p = [(i,v) for i,v in enumerate(priorities)]
    l = []
    
    while p:
        a = p.pop(0)
        if not p:
            l.append(a)
            break
            
        if a[1]>=max([j[1] for j in p]):
            l.append(a)
        else:
            p.append(a)
    return l.index((location,priorities[location]))+1
 """참고 코드
 def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
"""
    
    
