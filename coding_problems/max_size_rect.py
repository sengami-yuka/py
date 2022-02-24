class Solution():
    def max_hist(self, row):
        result = []
        top_val = 0
        max_area = 0
        max_left = -1
        max_right = -1
        area = 0
        i = 0
        if row[1] == 0 or row[0] == 0 and row[2] == 0:
            return max_area, max_left, max_right
        while i < len(row):
            if not result or row[result[-1]] <= row[i]:
                result.append(i)
                i += 1
            else:
                left = result.pop()
                top_val = row[left]
                area = top_val * i
                if result:
                    left = result[-1] + 1
                    area = top_val * (i - left)
                if area > max_area:
                    max_area = area
                    max_left = left
                    max_right = i - 1
        while result:
            left = result.pop()
            top_val = row[left]
            area = top_val * i
            if result:
                left = result[-1] + 1
                area = top_val * (i - left)
            if area > max_area:
                max_area = area
                max_left = left
                max_right = len(row) - 1

        return max_area, max_left, max_right

    def max_hist2(self, row):
        max_area = 0
        max_left = -1
        max_right = -1
        for i in range(len(row)):
            h = row[i]
            if h == 0:
                continue
            left = i - 1
            right = i + 1
            while left >= 0 and row[left] >= h:
                left -= 1
            while right < len(row) and row[right] >= h:
                right += 1

            left += 1
            right -= 1

            area = h * (right - left + 1)
            if area > 1 and left == right:
                area = 1
            if area > max_area:
                max_area = area
                max_left = left
                max_right = right
        return max_area, max_left, max_right

    def max_rectangle(self, matrix):
        result, left, right = self.max_hist(matrix[0])
        top = 0
        bottom = 0

        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

            tmp_result, tmp_left, tmp_right = self.max_hist(matrix[i])
            if tmp_result > result or 12 == tmp_result == result and tmp_right - tmp_left < right - left:
                result = tmp_result
                left = tmp_left
                right = tmp_right
                bottom = i
                top = bottom - (result // (right - left + 1)) + 1
        return result, top, bottom, left, right


if __name__ == '__main__':
    A = [[0, 0, 0],
         [0, 0, 0],
         [1, 0, 0],
         [1, 1, 0],
         [0, 1, 0]]
    ans = Solution()
    for row in A:
        print(row)

    print("Area of maximum rectangle is", ans.max_rectangle(A))
