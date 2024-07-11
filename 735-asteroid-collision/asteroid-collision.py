class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1,len(asteroids)):
            stack.append(asteroids[i])
            while len(stack)>1:
                popped = stack.pop()
                top = stack[-1]
                sign = popped * top
                diff = abs(popped) - abs(top)
                if sign > 0:
                    stack.append(popped)
                    break
                elif top < 0:
                    stack.append(popped)
                    break
                else:
                    if diff == 0:
                        stack.pop()

                    elif diff > 0:
                        stack.pop()
                        stack.append(popped)
                    else:
                        pass
        return stack

            