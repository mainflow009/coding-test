class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s.reverse()
        answer = ""
        for i in s:
            if i != '':
                answer += i
                answer += ' '
        return answer[:-1]
