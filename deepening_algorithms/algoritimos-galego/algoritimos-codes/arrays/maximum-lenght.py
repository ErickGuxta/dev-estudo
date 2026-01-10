class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        _max = 1

        counter = {}
        counter[s[0]] = 1

        while r < len(s) -1:
            r+=1
            # verifica se o item ja ta no counter e incrementa ele
            if counter.get(s[r]):
                counter[s[r]] += 1
            # se não existe atribui o valor 1
            else:
                counter[s[r]] = 1

            while counter[s[r]] == 3:
                counter[s[l]] -= 1
                l += 1
            
            if r-l+1 > _max:
                _max = r-l+1
        
        
        return _max
