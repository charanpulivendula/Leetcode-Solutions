from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        res = 0
        while(len(self.queue1)>1) :
            self.queue2.append(self.queue1.popleft())
        res = self.queue1.popleft()
        self.queue1,self.queue2 = self.queue2,self.queue1
        return res
        

    def top(self) -> int:
        res = 0
        while(len(self.queue1)>1):
            print(self.queue1)
            self.queue2.append(self.queue1.popleft())
        res = self.queue1.popleft()
        self.queue2.append(res)
        self.queue1,self.queue2 = self.queue2,self.queue1
        return res
        

    def empty(self) -> bool:
        return len(self.queue1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()