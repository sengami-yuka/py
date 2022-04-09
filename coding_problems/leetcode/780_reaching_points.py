class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            if tx < ty:
                ty %= tx
            else:
                tx %= ty
        if sx > tx or sy > ty:
            return False
        return (ty - sy) % sx == 0 if sx == tx else (tx - sx) % sy == 0


solution = Solution()
assert solution.reachingPoints(1, 1, 3, 5)

assert not solution.reachingPoints(1, 1, 2, 2)

assert solution.reachingPoints(1, 1, 1, 1)
