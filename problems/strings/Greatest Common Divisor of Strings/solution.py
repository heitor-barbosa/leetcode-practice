# First Submission - O(n+m)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) > len(str2):
            biggest_str = str1
            smallest_str = str2
        else:
            biggest_str = str2
            smallest_str = str1

        for i in range(len(smallest_str), -1, -1):
            substr = smallest_str[:i]

            if not (biggest_str.replace(substr, '')) and not (smallest_str.replace(substr, '')):
                return substr
        
        return ''


# Second / Optimal Submission - O(n+m)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ''

        import math
        gcd = math.gcd(len(str1), len(str2))

        return str1[:gcd]
