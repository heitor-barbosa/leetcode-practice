# First Submission - time O(n) / space O(1)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = candies[0]
        for candy in candies:
            if candy > greatest:
                greatest = candy

        result = [] 
        for candy in candies:
            result.append(candy + extraCandies >= greatest)
        
        return result