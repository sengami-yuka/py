from typing import List


class Solution:  # DP
    def trap(self, height: List[int]) -> int:
        L = len(height)
        if L < 3:
            return 0
        ans = 0
        left_max = height[0]
        right_max_list = height[:]
        for i in range(L - 2, 0, -1):
            right_max_list[i] = max(right_max_list[i], right_max_list[i + 1])
        for i in range(1, L - 1):
            cur = height[i]
            if left_max > cur:
                right_max = right_max_list[i]
                if right_max > cur:
                    ans += min(left_max, right_max) - cur
            elif cur > left_max:
                left_max = cur
        return ans


class Solution2:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        if L < 3:
            return 0
        ans = 0
        st = []
        for i in range(L):
            while st and height[i] > height[st[-1]]:
                j = st.pop()
                if st:
                    ans += (min(height[i], height[st[-1]]) - height[j]) * (i - st[-1] - 1)
            st.append(i)
            print(st)
        return ans


class Solution3:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        while left < right:
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                ans += rightMax - height[right]
                right -= 1
                rightMax = max(rightMax, height[right])
        return ans


solution = Solution3()
ans = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
assert ans == 6, ans

ans = solution.trap([4,2,0,3,2,5])
assert ans == 9, ans
