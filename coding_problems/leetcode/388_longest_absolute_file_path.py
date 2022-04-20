class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans = 0
        s = ''
        is_file = False
        st = []
        tabs = 0
        input += '\n'
        for c in input:
            if c == '\n':
                for _ in range(tabs, len(st)):
                    st.pop()
                if is_file:
                    if st:
                        ans = max(ans, st[-1] + len(s))
                    else:
                        ans = max(ans, len(s))
                else:
                    if st:
                        st.append(st[-1] + len(s) + 1)
                    else:
                        st.append(len(s) + 1)
                tabs = 0
                s = ''
                is_file = False
            elif c == '\t':
                tabs += 1
            else:
                s += c
                if c == '.':
                    is_file = True
        return ans


class Solution2:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        depth_length_map = {-1: 0}
        for line in input.split('\n'):
            depth = line.count('\t')
            depth_length_map[depth] = depth_length_map[depth - 1] + len(line) - depth
            if '.' in line:
                res = max(res, depth_length_map[depth] + depth)
        return res


solution = Solution2()
ans = solution.lengthLongestPath('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext')
assert ans == 20, ans

ans = solution.lengthLongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')
assert ans == 32, ans

ans = solution.lengthLongestPath('a')
assert ans == 0, ans

ans = solution.lengthLongestPath('file1.txt\nfile2.txt\nlongfile.txt')
assert ans == 12, ans
