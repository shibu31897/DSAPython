class BubbleSort:
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)
        print(f"The original list is : {nums}")

    def sort(self):
        n = len(self.nums)
        aList = self.nums
        for i in range(n):
            for j in range(0,n-i-1):
                if aList[j]>aList[j+1]:
                    aList[j],aList[j+1] = aList[j+1],aList[j]
        return aList




sort = BubbleSort([99,87,66,55,12,1,0])
print(sort.sort())