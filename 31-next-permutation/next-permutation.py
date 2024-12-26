class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = len(nums)-2
        while(index>=0):
            if nums[index]>=nums[index+1]:
                index-=1
            else:
                break
        # print(index)
        if index>=0:
            mini = float('inf')
            minIndex = index
            for j in range(index+1,len(nums)):
                if nums[j]>nums[index]:
                    if nums[j]<mini:
                        mini = nums[j]
                        minIndex = j
            nums[index],nums[minIndex] = nums[minIndex],nums[index]
            for j in range(index+1,len(nums)):
                findmin = nums[j]
                indexMini = j
                for k in range(j+1,len(nums)):
                    if nums[k]<findmin:
                        findmin = nums[k]
                        indexMini = k
                nums[j],nums[indexMini] = nums[indexMini],nums[j]
            return nums

            return nums
        else:
            nums.sort()
            return nums
        