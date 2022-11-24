'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.li = nums[:k]
        self.li.sort(reverse=True)
        for n in nums[k:]:
            self.add(n)
    
    def add(self, val: int) -> int:
        if len(self.li) < self.k or val > self.li[-1]:
            self._insert(val)
        return self.li[-1]
    
    def _insert(self, val):
        left = 0
        right = len(self.li)
        while left < right:
            mid = left + (right - left) // 2
            if val == self.li[mid]:
                left = mid
                right = mid
            elif val < self.li[mid]:
                left = mid + 1
            else:
                right = mid
        self.li.insert(left, val)
        if len(self.li) > self.k:
            self.li.pop(-1)
