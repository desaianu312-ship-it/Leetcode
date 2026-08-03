class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        nextGreater = {}

        for num in nums2:

            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num

            stack.append(num)

        while stack:
            nextGreater[stack.pop()] = -1

        return [nextGreater[num] for num in nums1]