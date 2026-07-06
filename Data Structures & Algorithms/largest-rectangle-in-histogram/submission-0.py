class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mx = 0
        s = []              # (i, h)
        for i, h in enumerate(heights):
            start = i
            while s and s[-1][1] > h:
                idx, height = s.pop()
                mx = max(mx, height * (i - idx))
                start = idx
            s.append((start, h))

        for i, h in s:
            mx = max(mx, h * (len(heights) - i))
        return mx