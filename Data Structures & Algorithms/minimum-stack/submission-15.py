class MinStack:

    def __init__(self):
        self.storage = [] # meant to be stack but accidently called storage
        self.minStack = []
        # for minStack, basically if min of whats seen before, then add to end of list, else just append the original value ie minStack[-1] is always the min.
        

    def push(self, val: int) -> None:
        self.storage.append(val)
        # check if min of minStack:
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
        

    def pop(self) -> None:
        if not self.storage:
            return
        self.storage.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        if self.storage:
            return self.storage[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
