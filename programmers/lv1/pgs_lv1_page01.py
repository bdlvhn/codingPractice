"""크레인 인형뽑기 게임"""
def solution(board, moves):
    board_tf = [list(filter(lambda x:x>0,i)) for i in zip(*board)]
    stack = [0]
    cnt = 0
    
    for move in moves:
    	if len(board_tf[move-1])>0:
    		stack.append(board_tf[move-1].pop(0))
    	if len(stack)>1:
    		if stack[-1]==stack[-2]:
	    		stack = stack[:-2]
	    		cnt += 2
            
    return cnt


"""두 개 뽑아서 더하기"""
from itertools import combinations

def solution(numbers):
    l = list(combinations(numbers,2))
    return sorted(list(set(map(lambda x: sum(x),l))))


"""완주하지 못한 선수"""
import collections

def solution(participant, completion):
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    
    return (list((p-c))[0])


"""모의고사"""
def solution(answers):
    answer = [0,0,0]

    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]

    for i,v in enumerate(answers):
    	d = [int(n1[i%len(n1)]==v),int(n2[i%len(n2)]==v),int(n3[i%len(n3)]==v)]
    	answer = list(map(lambda x: sum(x), zip(answer,d)))

    return [i+1 for i,v in enumerate(answer) if v == max(answer)]


"""k번째 수"""
def solution(array, commands):
    answer = []

    for c in commands:
    	answer.append(sorted(array[(c[0]-1):c[1]])[c[2]-1])

    return answer


"""체육복"""
def solution(n, lost, reserve):

    student = [-99] + [1] * n + [-99]
    for i in lost:
    	student[i] -= 1
    for j in reserve:
    	student[j] += 1

    rich = list(filter(lambda x:student[x]==2,range(1,n+1)))

    for k in rich:
    	if student[k-1] == 0:
    		student[k-1] += 1
    		student[k] -= 1
    	elif student[k+1] == 0:
    		student[k+1] += 1
    		student[k] -= 1

    return len(list(filter(lambda x: x>0, student)))


"""2016년"""
import datetime

def solution(a, b):
    return datetime.datetime(2016,a,b).strftime('%a').upper()


"""가운데 글자 가져오기"""
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]


"""3진법 뒤집기"""
import math
def solution(n):
    s = ''
    answer = 0
    for i in range(int(math.log(n,3)),-1,-1):
        s = s + str(n//(3**i))
        n -= (3**i)*(n//(3**i))
    s = s[::-1]
    print(s)
    for j in range(len(s)):
        answer += int(s[-(j+1)])*(3**j)
    return answer


"""같은 숫자는 싫어"""
from collections import deque

def solution(arr):
    ans = [-1]
    arr = deque(arr)
    while(len(arr)>0):
        a = arr.popleft()
        if ans[-1] != a:
            ans.append(a)
            
    return ans[1:]


"""같은 숫자는 싫어"""
 def solution(arr, divisor):
    ans = list(filter(lambda x: x%divisor==0,arr))
    return sorted(ans) if len(ans)>0 else [-1]


"""두 정수 사이의 합"""
def solution(a, b):
    return sum([i for i in range(min(a,b),max(a,b)+1)])


"""문자열 내 마음대로 정렬하기"""
def solution(strings, n):
    return sorted(strings,key=lambda x:(x[n],x))


"""문자열 내 p와 y의 개수"""
def solution(s):
    return s.lower().count('p') == s.lower().count('y')


"""문자열 내림차순으로 배치하기"""
def solution(s):
    return ''.join(sorted([i for i in s],reverse=True))


"""문자열 다루기 기본"""
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()


"""서울에서 김서방 찾기"""
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))


"""소수 찾기"""
def isPrime(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    return primes

def solution(n):
    return len(isPrime(n))


"""수박수박수박수박수박수?"""
def solution(n):
    return "수박"*(n//2) + "수"*(n%2)


"""문자열을 정수로 바꾸기"""
def solution(s):
    return int(s[1:]) if s[0]=='+' else int(s)
