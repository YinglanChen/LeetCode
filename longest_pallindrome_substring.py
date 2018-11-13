class Solution:
    # max_len is actually max_half_len
    def oddPalindrome(self,s, center):
        max_len = 0
        valid_range = min(center, len(s) - center - 1)
        for i in range(valid_range):
            if (s[center-i] == s[center+i]):
                max_len+=1
            else:
                break
        return max_len

    def evenPalindrome(self, s, center):
        if (center == len(s) - 1): return -1
        max_len = 0
        valid_range = min(center, len(s)-(center+1)-1)
        for i in range(valid_range):
            if (s[center-i] == s[center+1+i]):
                max_len+=1
            else:
                break
        return max_len
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = -1
        max_str = ""
        for center in range(0,len(s)):
            odd_len = self.oddPalindrome(s, center)
            if (odd_len > max_len):
                max_len = odd_len
                max_str = s[center-max_len: center+max_len+1]
            even_len = self.evenPalindrome(s, center)
            if (even_len > max_len):
                max_len = even_len
                max_str = s[center-max_len:center+1+max_len+1]
        return max_str
        