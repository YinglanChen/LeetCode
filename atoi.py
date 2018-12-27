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
            if (c == ' '): 
                if (not has_start):
                    continue
                else:
                    break
            if (c == '+'):
                if (has_start): 
                    break
                sign = 1
                has_start = True
                continue
            if (c == '-'): 
                if (has_start): break
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
        