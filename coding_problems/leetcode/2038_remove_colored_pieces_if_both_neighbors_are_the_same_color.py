class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b, cur = 0, 0, 0
        for c in colors:
            if c == 'A':
                if cur >= 0:
                    cur += 1
                    if cur >= 3:
                        a += 1
                else:
                    cur = 1
            else:
                if cur <= 0:
                    cur -= 1
                    if cur <= -3:
                        b += 1
                else:
                    cur = -1
        return a > b
