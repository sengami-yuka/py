# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
import re


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def process(elem):
            if type(elem) == int:
                return NestedInteger(elem)
            lst = NestedInteger()
            for c in elem:
                lst.add(process(c))
            return lst
        return process(eval(s))


class Solution2:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        ls = re.split(r'([\[\],])', s)
        stk = []
        for ch in ls:
            if ch == '[':
                stk.append(NestedInteger())
            elif ch == ']':
                ni = stk.pop()
                if stk:
                    stk[-1].add(ni)
            elif ch and ch != ',':
                stk[-1].add(NestedInteger(int(ch)))
        return ni


class Solution3:
    def deserialize(self, s: str) -> NestedInteger:
        index = 0

        def dfs() -> NestedInteger:
            nonlocal index
            if s[index] == '[':
                index += 1
                ni = NestedInteger()
                while s[index] != ']':
                    ni.add(dfs())
                    if s[index] == ',':
                        index += 1
                index += 1
                return ni
            else:
                negative = False
                if s[index] == '-':
                    negative = True
                    index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    num *= 10
                    num += int(s[index])
                    index += 1
                if negative:
                    num = -num
                return NestedInteger(num)

        return dfs()


class Solution4:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack, num, negative = [], 0, False
        for i, c in enumerate(s):
            if c == '-':
                negative = True
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(NestedInteger())
            elif c in ',]':
                if s[i-1].isdigit():
                    if negative:
                        num = -num
                    stack[-1].add(NestedInteger(num))
                num, negative = 0, False
                if c == ']' and len(stack) > 1:
                    stack[-2].add(stack.pop())
        return stack.pop()


class Solution5:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = []
        # num为数字，sign为符号为，is_num为前一个是否为数字
        num, sign, is_num = 0, 1, False
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                is_num = True
            elif c == '-':
                sign = -1
            elif c == '[':
                stack.append(NestedInteger())
            elif c == ',' or c == ']':
                # 把刚才遇到的数字append进去
                if is_num:
                    cur_list = stack.pop()
                    cur_list.add(NestedInteger(sign * num))
                    stack.append(cur_list)
                num, sign, is_num = 0, 1, False
                # 此时为嵌套列表
                if c == ']' and len(stack) > 1:
                    cur_list = stack.pop()
                    stack[-1].add(cur_list)
        return stack[0]


solution = Solution()
solution.deserialize('324')
solution.deserialize('[123,[456,[789]]]')
solution.deserialize('[123,456,[788,799,833],[[]],10,[]]')
