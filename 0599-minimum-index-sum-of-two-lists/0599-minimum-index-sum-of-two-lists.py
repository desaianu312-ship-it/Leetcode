class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {restaurant: i for i, restaurant in enumerate(list1)}

        min_sum = float("inf")
        result = []

        for j, restaurant in enumerate(list2):
            if restaurant in index:
                total = index[restaurant] + j

                if total < min_sum:
                    min_sum = total
                    result = [restaurant]
                elif total == min_sum:
                    result.append(restaurant)

        return result
        
        