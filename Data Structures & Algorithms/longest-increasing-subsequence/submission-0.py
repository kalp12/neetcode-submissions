class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]]
        max_len = 1
        for num in nums:
            if num > lst[-1]:
                lst.append(num)
                max_len += 1
            else:
                ind = 0
                while ind < len(lst) and lst[ind] < num:
                    ind += 1
                lst[ind] = num
        return max_len