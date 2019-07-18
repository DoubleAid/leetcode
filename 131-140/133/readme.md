## 题目
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

## 用例
### Example:
1---2  
|   |  
|   |  
4---3  

#### Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

#### Explanation:
+ Node 1's value is 1, and it has two neighbors: Node 2 and 4.
+ Node 2's value is 2, and it has two neighbors: Node 1 and 3.
+ Node 3's value is 3, and it has two neighbors: Node 2 and 4.
+ Node 4's value is 4, and it has two neighbors: Node 1 and 3.

## 方法一
### 想法
使用队列进行广度优先遍历，将便利完的值标记为对应的新图的节点值
```
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        result = Node(0,[])
        temp = [[node,result]]
        while temp:
            source,target = temp.pop(0)
            if type(source.val)!=int:
                target.neighbors.append(source.val)
                continue
            newNode = Node(source.val,[])
            target.neighbors.append(newNode)
            source.val = newNode
            for i in source.neighbors:
                temp.append([i,newNode])
        return result.neighbors[0]
        

```
