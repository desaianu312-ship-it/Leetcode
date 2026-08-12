class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.nums = nums

        for i in range(self.n):
            self._update(i + 1, nums[i])

    def _update(self, i, value):
        while i <= self.n:
            self.tree[i] += value
            i += i & -i

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._update(index + 1, diff)

    def _query(self, i):
        total = 0

        while i > 0:
            total += self.tree[i]
            i -= i & -i

        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)