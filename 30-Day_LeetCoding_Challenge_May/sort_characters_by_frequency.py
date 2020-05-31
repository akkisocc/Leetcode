from collections import defaultdict as dd
"""
Input : "tree" -> eert, eetr
        "" -> ?
        
        
Steps:
1. Use hashmap to store the frequency of each char
2. Sort the frequency in decreasing order and print it
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        m1 = dd(int)
        for i in s:
            m1[i]+=1
        res=sorted(m1.items(),key=lambda x : x[1],reverse=True)
        output=""
        for key, value in res:
            for _ in range(value):
                output+=key
        return output
