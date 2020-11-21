""" 기능개발 """
import math

def solution(progresses, speeds):
	l = [math.ceil((100-a)/b) for a,b in zip(progresses,speeds)]
	ans = []

	while l:
		t = [i<=l[0] for i in l]
		if list(filter(lambda x:x>l[0],l)):
			ans.append(t.index(False))
			l = l[t.index(False):]
		else:
			ans.append(len(t))
			l = []
	return ans

""" 참고 코드
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
"""
   
""" 다리를 지나는 트럭 """
