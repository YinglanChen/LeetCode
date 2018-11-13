class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1): return s
        num  = len(s)
        group = numRows - 1
        numCols = (num // (2*numRows - 2) + 1) * (numRows - 1)
        matrix = [["" for i in range(numCols)] for j in range(numRows)]
        r = 0
        c = 0
        for char in s:
            matrix[r][c] = char
            # case 1
            if (c % group == 0):
                if (r == numRows-1):
                    c += 1
                    r -= 1
                else:
                    r += 1
            # case 2
            else:
                c += 1
                r -= 1
        result = ""
        for r in range(numRows):
            for c in range(numCols):
                result += matrix[r][c]
        return result