class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=set()
        for i in range(len(numbers)):
            if numbers[i] not in s:
                s.add(numbers[i])
                j=i+1
                n=target-numbers[i]
                
                while j<=len(numbers)-1:
                    if numbers[j]==n:
                        return [i+1,j+1]
                    j+=1
