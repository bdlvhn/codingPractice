"""시저 암호"""
def solution(s, n):
    l = []

    for char in s:
    	if ord(char)>=65 and ord(char)<=90:
    		l.append(chr(65+(ord(char)-65+n)%26))
    	elif ord(char)>=97 and ord(char)<=122:
    		l.append(chr(97+(ord(char)-97+n)%26))
    	else:
    		l.append(' ')
    return ''.join(l)


"""약수의 합"""
import math
def solution(n):
	a = []

	for i in range(1,int(math.sqrt(n))+1):
		if n%i == 0:
			a.append(i)
			a.append(n/i)
	return sum(set(a))


"""이상한 문자 만들기"""
def solution(s):
    cnt = 0
    l = []

    for word in s:
        if word.isalpha():
        	cnt += 1
        	if cnt%2==0:
        		l.append(word.lower())
        	else:
        		l.append(word.upper())


        else:
        	cnt = 0
        	l.append(word)

    return ''.join(l)
""" 참고 코드
def toWeirdCase(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])
"""


"""자릿수 더하기"""
def solution(n):
    return sum([int(s) for s in str(n)])


"""참고 코드
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 
"""


"""자연수 뒤집어 배열로 만들기"""
def solution(n):
    return [int(i) for i in str(n)[::-1]]


"""정수 내림차순으로 배치하기"""
def solution(n):
    return int(''.join(sorted(list(map(lambda x:x,str(n))),reverse=True)))


"""정수 제곱근 판별"""
def solution(n):
    return (n**0.5+1)**2 if n**0.5%1==0 else -1


""" 제일 작은 수 제거하기"""
def solution(arr):
    arr.pop(arr.index(min(arr)))
    return arr if arr else [-1]


"""짝수와 홀수"""
def solution(num):
    return "Odd" if num%2==1 else "Even"


"""키패드 누르기"""
def solution(numbers, hand):

	dict = {'1':[0,3],'2':[1,3],'3':[2,3],
	'4':[0,2],'5':[1,2],'6':[2,2],
	'7':[0,1],'8':[1,1],'9':[2,1],
	'*':[0,0],'0':[1,0],'#':[2,0],
	'left':['L',0],'right':['R',1]}
	position = [dict['*'],dict['#']]
	ans = []
	
	for num in numbers:
		if num in [1,4,7]:
			ans.append('L')
			position[0] = dict[str(num)]
		elif num in [3,6,9]:
			ans.append('R')
			position[1] = dict[str(num)]
		else:
			l_dist = abs(position[0][0]-dict[str(num)][0]) + \
					 abs(position[0][1]-dict[str(num)][1])
			r_dist = abs(position[1][0]-dict[str(num)][0]) + \
					 abs(position[1][1]-dict[str(num)][1])
			if l_dist < r_dist:
				ans.append('L')
				position[0] = dict[str(num)]
			elif l_dist > r_dist: 
				ans.append('R')
				position[1] = dict[str(num)]
			else:
				ans.append(dict[hand][0])
				position[dict[hand][1]] = dict[str(num)]

	return ''.join(ans)
