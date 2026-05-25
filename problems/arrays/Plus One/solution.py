# First Submission - time O(n²) / space O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = ''
        for n in digits:
            num += str(n)
            
        num = int(num)
        num += 1
        num = str(num)
        
        result = []
        for c in num:
            result.append(int(c))
        
        return result
    

# Second Submission - time O(n) / space O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        
        i = n - 1
        digits[i] += 1

        while(digits[i] > 9):
            digits[i] = 0

            if i-1 >= 0:                        # theres still more array
                digits[i-1] += 1
            else:                               # end of the array
                return [1] + digits

            i -= 1

        return digits
    

# Optimal Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits