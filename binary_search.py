from copy import deepcopy
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[-1] > 0 and nums[-1] < target:
            return -1
        
        if nums[-1] < 0 and nums[-1] > target:
            return -1
        
        subarray = deepcopy(nums)
        
        while True:
            
            subarray_len = len(subarray)
            middle_index = int(subarray_len / 2)
            
            
            if subarray[middle_index] == target:
                return middle_index

            if subarray[middle_index] > target:
                subarray = deepcopy(subarray[0 : middle_index])
                if len(subarray)==1:
                    return -1
                continue
                
            if subarray[middle_index] < target:
                subarray = deepcopy(subarray[middle_index : ])
                if len(subarray)==1:
                    return -1
                continue

if __name__ == '__main__':
    case = [-1,0,3,5,9,12]
    target = 9
    s = Solution()
    print(s.search(nums=case, target=target))