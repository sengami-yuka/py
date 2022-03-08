from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (x[0], -x[1]))
        L = len(people)
        ans = [0] * L
        for p in people:
            step = p[1]
            for j in range(L):
                if not ans[j]:
                    if step <= 0:
                        ans[j] = p
                        break
                    step -= 1
        return ans


class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        n = len(people)
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person]
        return ans


solution = Solution2()
assert [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] == solution.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
assert [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]] == solution.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]])
