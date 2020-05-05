class Solution:
    def findLen(self,a,zeros,ones):
        #print(ones,'--',zeros)
        if len(a)==0:
            return 0
        output=0
        if zeros == ones:
            #print(ones,'--',zeros)
            return len(a)
        
        
        if zeros> ones:
            if a[0] ==0 and a[-1]!=0:
                zeros-=1
                output += self.findLen(a[1:],zeros,ones)
                return output
            elif a[-1] == 0 and a[0]!=0:
                zeros-=1
                output +=self.findLen(a[:len(a)-1],zeros,ones)
                return output
            #print(a)
            
        if ones>zeros:
            if a[0] == 1 and a[0]!=1:
                ones-=1
                output += self.findLen(a[1:],zeros,ones)
                return output
            elif a[-1] == 1 and a[0]!=1:
                ones-=1
                output +=self.findLen(a[:len(a)-1],zeros,ones)
                return output
        if a[0] == 1 and a[-1] == 1:
            ones-=1
            output1= self.findLen(a[1:],zeros,ones)
            output2= self.findLen(a[:len(a)-1],zeros,ones)
            output+= max(output1,output2)
            #print(a)
            return output
        if a[0] == 0 and a[-1] == 0:
            zeros-=1
            output1= self.findLen(a[1:],zeros,ones)
            output2= self.findLen(a[:len(a)-1],zeros,ones)
            output+= max(output1,output2)
            #print(a)
            return output
        
        return output
                
    def findMaxLength(self, a: List[int]) -> int:
        zeros,ones=0,0
        n = len(a)
        for i in range(n):
            if a[i]==0:
                zeros+=1
            else:
                ones+=1
        
        return self.findLen(a,zeros,ones)
                
        
