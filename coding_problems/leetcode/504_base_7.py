import collections


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        ans = collections.deque()
        if num < 0:
            num = -num
            neg = 1
        else:
            neg = 0
        while num:
            num, rem = divmod(num, 7)
            ans.appendleft(str(rem))
        if neg:
            ans.appendleft('-')
        return ''.join(ans)


solution = Solution()
assert '202' == solution.convertToBase7(100)
assert '-10' == solution.convertToBase7(-7)
