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


