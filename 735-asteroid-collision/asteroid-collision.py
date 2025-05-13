class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for asteroid in asteroids[1:]:
            while stack and asteroid<0<stack[-1]:
                top = stack[-1]
                if top == -asteroid:
                    stack.pop()
                    break
                elif top<-asteroid:
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroid)
        return stack
                    

                



        

            