class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies in the list
        greatest_nb_candies = max(candies)
        # Initiate the list to ouput True/False
        greatest_nb_candies_with_extraCandies = []
        for child_candies in candies:
            # If the child candies + extraCandies is greater or equal than the maximum number of candies of a child
            if child_candies + extraCandies >= greatest_nb_candies:
                # If it's the case, append True
                greatest_nb_candies_with_extraCandies.append(True)
            else:
                # If it's NOT the case, append True
                greatest_nb_candies_with_extraCandies.append(False)
        return greatest_nb_candies_with_extraCandies

        
        