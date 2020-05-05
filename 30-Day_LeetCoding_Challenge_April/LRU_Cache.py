from collections import OrderedDict as od

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = od()
       
        

    def get(self, key: int) -> int:
        #print("get..")
        if self.cache.get(key)==None:
            return -1
        self.temp = self.cache[key]
        del self.cache[key]
        self.cache[key]=self.temp
        #print(self.cache)
        return self.cache[key]
        
                    

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key)!=None:
            del self.cache[key]
            self.cache[key]=value
            return
        if len(self.cache)==self.capacity:
            self.first = next(iter(self.cache))
            del self.cache[self.first]
            #print("after",self.cache)
        self.cache[key]=value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
