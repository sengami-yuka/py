from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        s = set(words)
        sw = sorted(words, key=lambda x: (-len(x), x))
        for word in sw:
            if len(word) == 1:
                return word
            for i in range(1, len(word)):
                if word[:-i] not in s:
                    break
            else:
                return word
        return ''


class Solution2:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word
                candidates.add(word)
        return longest


class Solution3:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        print(trie.root)
        ans = ""
        for word in words:
            if (len(word) > len(ans) or (len(word) == len(ans) and word < ans)) and trie.search(word):
                ans = word
        return ans


class Trie(object):
    def __init__(self):
        self.root = {'end': True}

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['end'] = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node or 'end' not in node:
                return False
            node = node[c]
        return 'end' in node


solution = Solution3()
assert 'world' == solution.longestWord(["w","wo","wor","worl","world"])
assert 'apple' == solution.longestWord(["a","banana","app","appl","ap","apply","apple"])
