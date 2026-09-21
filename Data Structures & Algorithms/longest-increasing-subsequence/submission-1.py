class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]]
        max_len = 1
        for num in nums:
            if num > lst[-1]:
                lst.append(num)
                max_len += 1
            else:
                l = 0
                r = len(lst) - 1
                while l < r:
                    m = (l + r) // 2
                    if lst[m] < num:
                        l = m + 1
                    else: r = m
                lst[l] = num
        return max_len