'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find last element that is smaller than its following element
        swap_ind = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                swap_ind = i
                break
        if swap_ind == -1:
            nums.reverse()
        else:
            # Swap with first element greater than swap ind
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[swap_ind]:
                    nums[i], nums[swap_ind] = nums[swap_ind], nums[i]
                    break
            # Reverse everything after swap_ind
            i = swap_ind+1
            j = len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -=1
