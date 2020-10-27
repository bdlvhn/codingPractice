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
