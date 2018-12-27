"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary 
until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus 
sign followed by as many numerical digits as possible, and interprets them as 
a numerical value.

The string can contain additional characters after those that form the integral
 number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid
 integral number, or if no such sequence exists because either str is empty
  or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        answer = 0
        sign = 1
        has_start = False
        for c in str:
            if (c == ' ' and not has_start): 
                continue
            if (c == '+'):
                if (has_start): return 0
                sign = 1
                has_start = True
                continue
            if (c == '-'): 
                if (has_start): return 0
                sign = -1
                has_start = True
                continue
            if (c.isdigit()):
                answer = answer*10 + int(c)
                has_start = True
            else:
                break
            # check overflow
            if (answer*sign > INT_MAX):
                return INT_MAX
            if (answer*sign < INT_MIN):
                return INT_MIN
        return answer * sign

def stringToString(input):
    import json
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            str = stringToString(line);
            
            ret = Solution().myAtoi(str)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()