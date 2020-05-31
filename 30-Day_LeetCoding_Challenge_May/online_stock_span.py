"""
Input:- [100, 80, 60, 70, 60, 75, 85]
Intuition :- 
for 100 - 1
for 80 - 1
for 60 - 1
for 70 - 2
If we see for 70, then all we are concerned about is finding the first greater element than 70
In this case it is 80, now after 80 one elements is there smaller than 80.
Now if somehow we can find how many element are there after 80 till 70 which are smaller but in consecutive order 
the our problem is solved.
So basically if there is some bigger element than 80 in between , then that will be answer instead of 80 :)
suppose [100,80,90,60,70], then for 70 answer would be 90 not 80.
So we only have to maintain element in decreasing order, 
Stack can help here:
s = [],
index=-1,
let consider first element , index=1
s.top = None, push to stack
s= [100]
index=1
s.top> curr
push to stack , return ans as curr_index-s.top_index
s=[100,80]
index=2
push to stack , return ans as curr_index-s.top_index
s=[100,80,60]
index=3
s.top<=curr
 pop till s.top>curr,, ans will be curr_index-greater_index
s=[100,80,70] , Why we are doing this?? bcoz we want to find first greater element after curr
s=[100,80,70,60]

Time Complexity = O(N)  N-- Calls to stack
Space Complexity = O(N) For stack
"""


class StockSpanner:

    def __init__(self):
        self.s = []
        self.i = -1
        

    def next(self, price: int) -> int:
        
        self.i+=1
        #print(self.s,"--",self.i)
        x = (price,self.i)
        if len(self.s)==0:
            self.s.append(x)
            return 1
        else:
            while len(self.s)>0 and self.s[-1][0]<=price:
                self.s.pop()
            
            greater=None
            if len(self.s)>0:
                greater=self.s[-1]
            if greater==None:
                self.s.append(x)
                return self.i+1
            
            self.s.append(x)
            return self.i-greater[1]
            
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
