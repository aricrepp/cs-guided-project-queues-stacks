"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.

You already have a `Stack` class that you've implemented using a dynamic array.

Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.

*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""


class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack:
    def __init__(self):
        # Your code here
        self.stack = Stack()
        self.max = None

    def push(self, item):
        """Add a new item onto the top of our stack."""
        # Your code here
        self.stack.push(item)
        # update max is necessary
        if self.max < item:
            self.max = item

    def pop(self):
        """Remove and return the top item from our stack."""
        # Your code here
        item = self.stack.pop()
        # check if were removing the max
        # if item == max:
        #     new_max = self.find_max()
        #     self.max = new_max

        return self.stack.pop()

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        # Your code here
        # approach 1: pop everything off, find the max and pop it back in
        # trick, when we push it back on, we want everything to stay in the same order

        return self.max

    def find_max(self):
        values = []
        element = self.stack.pop()
        cur_max = None
        while element is not None:
            values.append(element)
            if cur_max is None or cur_max < element:
                cur_max = element
            element = self.stack.pop()

        for i in range(len(values) - 1, -1, -1):
            element = values[i]
            self.push(element)

        return cur_max


max_stack = MaxStack()
max_stack.push(1)
max_stack.push(2)
max_stack.push(3)
max = max_stack.get_max()
print(max == 3)
