class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.tryrest(s[l:r]) or self.tryrest(s[l+1:r+1])
            l += 1
            r -= 1
        
        return True
        
    def tryrest(self, rest) -> bool:
            l, r = 0, len(rest)-1
            while l < r:
                if rest[l] != rest[r]:
                    return False
                l+=1
                r-=1

            return True