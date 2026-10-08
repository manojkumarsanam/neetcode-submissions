class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary(left,right,tag):
            while(left<=right):
                mid = left+(right-left)//2
                if numbers[mid]==tag:
                    return mid
                elif numbers[mid]<tag:
                    left = mid+1   
                else:
                    right = mid-1
            return  -1

        for i in range(len(numbers)):
            c = target-numbers[i]
            k=binary(i+1,len(numbers)-1,c)
            if k!=-1:
                return [i+1,k+1]
        return [] 


        