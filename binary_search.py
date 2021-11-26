from copy import deepcopy
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[-1] > 0 and nums[-1] < target:
            return -1
        
        if nums[-1] < 0 and nums[-1] > target:
            return -1
        
        upper_bound = len(nums) -1
        lower_bound = 0
        middle_index = (upper_bound + lower_bound) // 2
        
        while True:
            middle_index = (upper_bound + lower_bound) // 2
            if nums[middle_index] == target:
                return middle_index

            if nums[middle_index] > target:
                upper_bound = middle_index
                if upper_bound == lower_bound: 
                    return -1   

                if upper_bound - lower_bound == 1:
                    if nums[upper_bound] == target:
                        return upper_bound
                    if nums[lower_bound] == target:
                        return lower_bound  
                    else:
                        return -1           
                continue
                
            if nums[middle_index] < target:
                lower_bound = middle_index
                if upper_bound == lower_bound: 
                    return -1  

                if upper_bound - lower_bound == 1:
                    if nums[upper_bound] == target:
                        return upper_bound
                    elif nums[lower_bound] == target:
                        return lower_bound
                    else:
                        return -1


                continue

if __name__ == '__main__':
    case = [-1,0,5]
    target = -1
    s = Solution()
    print(s.search(nums=case, target=target))