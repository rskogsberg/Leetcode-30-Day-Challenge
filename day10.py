#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.


class MinStack:
    def __init__(self):
        self.min=float('inf')
        self.stack = []
    
    def push(self, x):
        if x<=self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
    def pop(self):
        t = self.stack[-1]
        self.stack.pop()
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min