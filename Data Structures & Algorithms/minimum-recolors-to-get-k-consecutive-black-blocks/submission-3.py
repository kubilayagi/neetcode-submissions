class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        for i in range(0, k):
            if blocks[i] == 'W':
                white += 1
        minops = white
        print(minops)
        for j in range(k, len(blocks)):
            if blocks[j] == 'W':
                white += 1
            if blocks[j-k] == 'W':
                white -= 1
            minops = min(minops, white)

        return minops