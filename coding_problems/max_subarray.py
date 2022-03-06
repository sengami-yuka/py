def f(nums):
    ans = nums[0]
    L = len(nums)
    dp = [ans] + [0] * (L - 1)
    for i in range(1, L):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        ans = max(dp[i], ans)
    return ans


print(f([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
