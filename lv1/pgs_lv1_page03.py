"""실패율"""
from collections import Counter

def solution(N, stages):
    l = []
    s = Counter(stages)
    n = len(stages)
    
    for i in range(1,N+1):
        if n==0:
            l.append([i,0])
        else:
            l.append([i,s[i]/n])
            n -= s[i]
    return [j[0] for j in sorted(l,key=lambda x:(-x[1],x[0]))]


"""다트 게임"""
import re

def solution(dartResult):
    a = [0,0,0,0]
    p = re.compile('\d+\D+[*#]?')
    l = p.findall(dartResult)
    dict = {'S':1,'D':2,'T':3,'*':2,'#':-1}
    for i,val in enumerate(l):
        if val[:2] == '10':
            a[i] = int(val[:2])*dict[val[2]]
        else:
            a[i] = int(val[0])*dict[val[1]]
        
        if val[-1] == '*':
            a[i] = a[i] * dict[val[-1]]
            a[i-1] = a[i-1] * dict[val[-1]]
        if val[-1] == '#':
            a[i] = a[i] * dict[val[-1]]
    return sum(a)

"""참고 
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
"""
