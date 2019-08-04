## 题目
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

### Follow up:
Could you do both operations in O(1) time complexity?

## 用例
### Example:
```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```
## 方法一
### 想法
使用字典(哈西表)定位key对应的值
使用队列确定先后顺序
### time 20 memory 92
```
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
        self.keys = []

    def get(self, key):
        if key in self.data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.data[key]
        return -1

    def put(self, key, value):
        if key in self.data:
            self.keys.remove(key)
            self.keys.append(key)
            self.data[key] = value
        elif self.capacity == 0:
            oldkey = self.keys.pop(0)
            self.data.pop(oldkey)
            self.keys.append(key)
            self.data[key] = value
        else:
            self.keys.append(key)
            self.data[key] = value
            self.capacity -= 1
```
