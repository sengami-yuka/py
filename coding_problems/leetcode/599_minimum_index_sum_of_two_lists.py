from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        d = {v: i for i, v in enumerate(list1)}
        s = 9999
        for i, v, in enumerate(list2):
            if i > s:
                break
            if v in d:
                tmp = d[v] + i
                if tmp < s:
                    ans = [v]
                    s = tmp
                elif tmp == s:
                    ans.append(v)
        return ans


solution = Solution()
ans = solution.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
assert ans == ["Shogun"], ans

ans = solution.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])
assert ans == ["Shogun"], ans
