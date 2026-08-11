class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)

        mid = (n - 1) // 2
        right = n - 1

        temp = nums[:]

        for i in range(0, n, 2):
            nums[i] = temp[mid]
            mid -= 1

        for i in range(1, n, 2):
            nums[i] = temp[right]
            right -= 1
        """
        Do not return anything, modify nums in-place instead.
        """
        