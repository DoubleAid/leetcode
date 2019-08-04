## 题目
Implement the following operations of a stack using queues.

+ push(x) -- Push element x onto stack.
+ pop() -- Removes the element on top of the stack.
+ top() -- Get the top element.
+ empty() -- Return whether the stack is empty.
## 用例
### Example:
```
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```
### Notes:

+ You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
+ Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
+ You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
## 方法一
### 思路
我觉得里面最难的一点就是出栈了，我的解决方法是从头往后数，依次再把她们插入队列里面去，只有最后一个不插入
```
class MyStack(object):

def __init__(self):
"""
Initialize your data structure here.
"""
self.length = 0
self.queue = []


def push(self, x):
"""
Push element x onto stack.
:type x: int
:rtype: None
"""
self.queue.append(x)
self.length += 1


def pop(self):
for i in range(self.length-1):
val = self.queue.pop(0)
self.queue.append(val)
val = self.queue.pop(0)
self.length -= 1
return val


def top(self):
return self.queue[-1]


def empty(self):
if self.length > 0:
return False
return True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
