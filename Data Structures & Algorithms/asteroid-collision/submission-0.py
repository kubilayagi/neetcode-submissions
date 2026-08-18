class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if abs(a) > stack[-1]:
                    stack.pop()
                elif abs(a) < stack[-1]:
                    a = 0
                elif abs(a) == stack[-1]:
                    a = 0
                    stack.pop()
            if a != 0:
                stack.append(a)
        return stack
                
