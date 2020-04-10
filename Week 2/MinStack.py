"""
Task 10:
    Design a stack that supports push, pop, top, and retrieving 
    the minimum element in constant time.
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
    
    Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
"""
#18 / 18 test cases passed.
#Runtime: 804 ms
#Memory Usage: 17.4 MB

class MinStack:

    def __init__(self):
        self.stack = list()
        
    def push(self, x: int) -> None:
        self.stack.append(x)     
    def pop(self) -> None:
        self.stack.pop()   
    def top(self) -> int:
        return self.stack[-1]   
    def getMin(self) -> int:
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
#obj = MinStack()
#obj.push(x)
#obj.pop()
#param_3 = obj.top()
#param_4 = obj.getMin()
