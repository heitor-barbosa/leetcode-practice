# First Submission - O(n+m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            bigger_word_len = len(word1)
        else:
            bigger_word_len = len(word2)
        
        ans = ''

        for i in range(bigger_word_len):
            try:
                ans += word1[i]
            except:
                pass
            try:
                ans += word2[i]
            except:
                pass

        return ans
    

# Second Submission - O(n+m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        bigger_word_len = max(len(word1), len(word2))
        
        ans = []

        for i in range(bigger_word_len):
            if i < len(word1):
                ans.append(word1[i])
            
            if i < len(word2):
                ans.append(word2[i])

        return ''.join(ans)
    

# Two pointer solution by Leetcode - O(n+m)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)