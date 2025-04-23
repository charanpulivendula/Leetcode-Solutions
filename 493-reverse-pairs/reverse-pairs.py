class Solution:
    def __init__(self):
        self.count = 0
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        def mergesort(nums,left,right):
            if left>=right:
                return
            mid = (left+right)//2
            mergesort(nums,left,mid)
            mergesort(nums,mid+1,right)
            
            merge(nums,left,mid,right)

        def merge(nums,left,mid,right):
            first = nums[left:mid+1]
            second = nums[mid+1:right+1]
            m = len(first)
            n = len(second)
            ptr = 0
            for i in range(len(first)):
                while(ptr<n and first[i]>2*second[ptr]):
                    ptr+=1
                self.count+=(ptr)
            i = 0
            j = 0
            k = left
            while(i<m and j<n):
                if first[i]<=second[j]:
                    nums[k] = first[i]
                    i+=1
                else:
                    nums[k]=second[j]
                    j+=1
                k+=1
            
            while(i<m):
                nums[k] = first[i]
                i+=1
                k+=1
            while(j<n):
                nums[k] = second[j]
                j+=1
                k+=1
            
        mergesort(nums,0,len(nums)-1)
        return self.count

            


        
