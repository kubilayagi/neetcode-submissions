class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                # there are no ways to decode a string that starts with zero.
                # this makes sense for how we are building this solution because
                # we are going from back to front. so if s[i] == '0', that means
                # our strings start with zero, which is invalid
                dp[i] = 0
            else:
                # say that there were only digits 1-9. that would mean that every string
                # only has one way to decode it (except those that start with 0). if this
                # is the case, then as we build up the solution, each position in the dp will be
                # one because there is only one way to do this. we handle the possibility of the current
                # number being combined with the previous number in the next case
                dp[i] = dp[i+1]

            # we check that the char to the right is in bounds because we don't need to check this possibility
            # for a string of length 1
            # for s[i] == 1, we don't need to check the second digit because all of them are allowed.
            # for s[i] == 2, there are restrictions. they can only be between 0-6
            if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                # we also need to handle the possibility that our current number is actually a two digit number
                # so we already added the number of possibilities to decode assuming it was a one digit number in the
                # step above. this case adds on the extra ways to decode if the current number is actually part of a two
                # digit number
                dp[i] += dp[i+2]

        return dp[0]
            