class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            odd = expand_around_center(i, i)
            even = expand_around_center(i, i + 1)
            longer = odd if len(odd) > len(even) else even
            if len(longer) > len(longest):
                longest = longer
        return longest


        