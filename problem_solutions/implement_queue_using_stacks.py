'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
'''
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def build_s2(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1[-1])
                self.s1.pop(-1)

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.build_s2()
        val = self.s2[-1]
        self.s2.pop(-1)
        return val

    def peek(self) -> int:
        self.build_s2()
        return self.s2[-1]

    def empty(self) -> bool:
        return not (self.s1 or self.s2)
