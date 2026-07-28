class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        count = Counter(s)
        first_half = []
        middle = ""
        
        for ch in sorted(count.keys()):
            freq = count[ch]
            
            first_half.append(ch * (freq // 2))
            
            if freq % 2 == 1:
                middle = ch
        
        first_half = "".join(first_half)
        
        return first_half + middle + first_half[::-1]