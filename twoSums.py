class TwoSum:
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target

    def finSums(self):      
        for i in range(0,len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i,j]


twoSum = TwoSum(nums=[1,3,4,5,6,7],target=8)
print(twoSum.finSums())