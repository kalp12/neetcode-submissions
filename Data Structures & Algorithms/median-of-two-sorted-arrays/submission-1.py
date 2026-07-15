class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        len1 = len(nums1)
        len2 = len(nums2)
        left = 0
        right = len1

        while left <= right:
            part1 = (left + right) // 2
            part2 = (len1 + len2 + 1) // 2 - part1

            mx_left1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            mn_right1 = float('inf') if part1 == len1 else nums1[part1]
            mx_left2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            mn_right2 = float('inf') if part2 == len2 else nums2[part2]

            if mx_left1 <= mn_right2 and mx_left2 <= mn_right1:
                if (len1 + len2) % 2 == 0:
                    return (max(mx_left1, mx_left2) + min(mn_right1, mn_right2)) / 2
                else:
                    return max(mx_left1, mx_left2)
            elif mx_left1 > mn_right2:
                right = part1 - 1
            else: left = part1 + 1