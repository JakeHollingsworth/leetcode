'''
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
'''
class Foo:
    def __init__(self):
        self.boolFirst = False
        self.boolSecond = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.boolFirst = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.boolFirst:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.boolSecond = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.boolSecond:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
