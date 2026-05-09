class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def dic(a):
            d=defaultdict(int)
            for i in a:
                if d[i]>0:
                    d[i]+=1
                else:
                    d[i]=1
            return d
        
        if dic(s)==dic(t):
            return True
        else:
            return False