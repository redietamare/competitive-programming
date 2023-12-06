class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        less = []
        more = []
        equal = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] == pivot:
                equal += 1
            else:
                more.append(nums[i])
        ans.extend(less)
        ans.extend([pivot]*equal)
        ans.extend(more)
        return ans