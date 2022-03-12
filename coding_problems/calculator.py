OP = {'+', '-', '*', '/'}


class Solution:
    def helper2(self, a):
        stack = []
        i = 0
        for i in a:
            if i == ')':
                j = len(stack) - 1
                while stack[j] != '(':
                    j -= 1
                res = self.helper(stack[j+1:])
                stack = stack[:j]
                stack.append(res)
            else:
                stack.append(i)
        return self.helper(stack)

    def helper(self, a) -> int:
        sign = '+'
        stack = []
        last = len(a) - 1
        num = 0
        for i, v in enumerate(a):
            if type(v) == int:
                num = v
            if i == last or v in OP:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = v
        return sum(stack)

    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        a = []
        d = ''
        last = len(s) - 1
        for i, c in enumerate(s):
            if c.isdigit():
                d += c
                if i == last:
                    a.append(int(d))
            else:
                if d:
                    a.append(int(d))
                    d = ''
                a.append(c)
        return self.helper2(a)


solution = Solution()
assert 7 == solution.calculate('3+2*2')
assert 1 == solution.calculate('3/2')
assert 5 == solution.calculate('3+5/2')
assert 2 == solution.calculate('1 + 1')
assert 3 == solution.calculate(' 2-1 + 2 ')
assert 23 == solution.calculate('(1+(4+5+2)-3)+(6+8)')
assert -1 == solution.calculate('-2+ 1')
assert -3 == solution.calculate('-(2+ 1)')
assert 13 == solution.calculate('14-3/2')
