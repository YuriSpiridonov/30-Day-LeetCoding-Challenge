"""
Task 24:
    Design and implement a data structure for Least Recently Used (LRU) cache. 
    It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key 
    exists in the cache, otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present. 
    When the cache reached its capacity, it should invalidate the least recently 
    used item before inserting a new item.
    
    The cache is initialized with a positive capacity.
    
    Follow up:
    Could you do both operations in O(1) time complexity?
    
    Example:
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
"""
#Difficulty: Medium
#18 / 18 test cases passed.
#Runtime: 1944 ms (slowest solution ever but it my first time/try to code caching algorithm)
#Memory Usage: 22.9 MB


import time
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.value_dict = dict()
        self.time_dict = dict()

    def get(self, key: int) -> int:
        if key in self.value_dict.keys(): self.time_dict[key] = time.time()
        return self.value_dict[key] if key in self.value_dict.keys() else -1
       
    def put(self, key: int, value: int) -> None:
        if len(self.value_dict) != self.capacity:
            self.value_dict[key] = value
            self.time_dict[key] = time.time()
        elif key in self.value_dict.keys():
            self.value_dict[key] = value
            self.time_dict[key] = time.time()
        else:
            del self.value_dict[min(self.time_dict.keys(), key=(lambda k: self.time_dict[k]))]
            del self.time_dict[min(self.time_dict.keys(), key=(lambda k: self.time_dict[k]))]
            self.value_dict[key] = value
            self.time_dict[key] = time.time()
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
