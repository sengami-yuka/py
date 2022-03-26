from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for op in ops:
            if op == 'D':
                arr.append(arr[-1] * 2)
            elif op == 'C':
                arr.pop()
            elif op == '+':
                arr.append(arr[-1] + arr[-2])
            else:
                arr.append(int(op))
        return sum(arr)
