class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        
        l, r = 0, n -1
        left_max, right_max = height[l], height[r]
        water = 0

        while l <= r:
            if left_max <= right_max:
                left_max = max(left_max, height[l])
                water += max(0, left_max - height[l])
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += max(0, right_max - height[r])
                r -= 1
        return water