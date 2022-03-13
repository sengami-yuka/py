from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        n = len(data)
        while i < n:
            cur = data[i]
            if cur & 192 == 192:
                length = 2
                if cur & 48 == 48:
                    length = 4
                elif cur & 32:
                    length = 3
                if cur & 1 << (7 - length):
                    # print(1, cur, bin(cur), length)
                    return False
                end = i + length
                i += 1
                while i < end:
                    try:
                        next = data[i]
                    except IndexError:
                        # print(2)
                        return False
                    if next & 192 != 128:
                        # print(3, next, bin(next), cur, bin(cur), length)
                        return False
                    i += 1
            elif cur & 128:
                # print(4)
                return False
            else:
                i += 1
        return True


solution = Solution()
assert solution.validUtf8([197,130,1])
assert not solution.validUtf8([235,140,4])
assert solution.validUtf8([194,155,231,184,185,246,176,131,161,222,174,227,162,134,241,154,168,185,218,178,229,187,139,246,178,187,139,204,146,225,148,179,245,139,172,134,193,156,233,131,154,240,166,188,190,216,150,230,145,144,240,167,140,163,221,190,238,168,139,241,154,159,164,199,170,224,173,140,244,182,143,134,206,181,227,172,141,241,146,159,170,202,134,230,142,163,244,172,140,191])
