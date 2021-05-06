import math
class MinStack(object):

    def __init__(self):
        """
        Time O(1)
        Space O(n)
        initialize your data structure here.
        """
        self.new_list = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.new_list.append(x)
        if not self.minstack:
            self.minstack.append(x)
        else:
            self.minstack.append(min(self.minstack[-1], x))

    def pop(self):
        """

        :rtype: None
        """
        self.new_list.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.new_list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(1)
    minStack.push(-3)
    min = minStack.getMin()
    print(min)
    minStack.pop()
    top = minStack.top()
    print(top)
    min = minStack.getMin()
    print(min)
