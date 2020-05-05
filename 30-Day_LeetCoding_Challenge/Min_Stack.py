import sys
class MinStack:

    def __init__(self):
    	self.s = list()
    	self.curr = sys.maxsize
    	self.small = sys.maxsize
        

    def push(self, x: int) -> None:
    	self.curr = x
    	self.small = min(self.curr,self.small)
    	self.temp =[]
    	self.temp.append(x)
    	self.temp.append(self.small)
    	self.s.append(self.temp)

    def pop(self) -> None:
        self.s.pop()
        if len(self.s)==0:
        	self.small = sys.maxsize
        else:
        	self.small = self.s[len(self.s)-1][1]

    def top(self) -> int:
        n=len(self.s)
        if n==0:
        	return -1
        return self.s[n-1][0]

    def getMin(self) -> int:
    	return self.s[len(self.s)-1][1]
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
