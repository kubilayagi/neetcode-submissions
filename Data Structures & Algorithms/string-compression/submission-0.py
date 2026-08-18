class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = k = 0
        while i < len(chars):
            c = chars[i]
            ccount = 1
            i += 1
            while i < len(chars) and chars[i] == c:
                ccount += 1
                i += 1
            
            if ccount > 1:
                kstr = c + str(ccount)
                for j in range(0, len(kstr)):
                    chars[k] = kstr[j]
                    k += 1
            else:
                chars[k] = c
                k += 1

        return k
