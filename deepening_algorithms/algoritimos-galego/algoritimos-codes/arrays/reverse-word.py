class Solution:
    def reverseWords(self, s: str) -> str:

        result = ""
        l, r = 0, 0

        while r < len((s)):
            if s[r] != " ":
                r += 1
            else:
                result += s[l:r][::-1]
                result += " "
                r +=1
                l = r

        result += s[l:r+2][::-1]

        return(result)

# com desempenho melhor:
class Solution:
    def reverseWords(self, s: str) -> str:
        res = " "
        for i in s.split():
            res += i[::-1]
            res += " "
        
        
        return(res[1:len(s) + 1])
