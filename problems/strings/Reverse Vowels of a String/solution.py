# First Submission
class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }

        x = []
        vowels_positions = []
        for i, char in enumerate(s):
            if char in VOWELS:
                x.append(char)
                vowels_positions.append(i)
        
        x.reverse()
        ans = list(s)

        for reversed_vowel, position in zip(x, vowels_positions):
            ans[position] = reversed_vowel
        
        return ''.join(ans)


        
