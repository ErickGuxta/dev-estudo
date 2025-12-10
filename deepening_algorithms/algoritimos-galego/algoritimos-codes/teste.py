from typing import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        ocorrencia = {}

        for i in range(len(s)):
            if ocorrencia.get(s[i]):
                ocorrencia[s[i]] +=1
            else:
                ocorrencia[s[i]] = 1
        
        for i in range(len(s)):
            if ocorrencia[s[i]] == 1:
                return i
        return -1