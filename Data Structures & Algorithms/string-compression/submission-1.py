class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        cur = None
        count = 0
        for c in chars:
            if not cur:
                cur = c
                count = 1
                continue  
            if cur != c:
                s = s + str(cur)
                if count > 1:
                    s = s + str(count)
                cur = c
                count = 1
            else:
                count += 1

        s = s + cur
        if count > 1:
            s = s + str(count)

        for i, c in enumerate(s):
            chars[i] = c
        return len(s)