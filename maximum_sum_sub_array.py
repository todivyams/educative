"""
Problem Statement#
Given an array of positive numbers and a positive number ‘k,’ find the maximum
sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

"""

##from itertools import combinations
##import time
##
##start = time.time()
##def max_sub_arr(arr,k):
##    max_sum = arr[0]
##    for item in list(combinations(arr,k)):
##        if max_sum < sum(item):
##           max_sum, max_sub = sum(item), item
##    print(max_sum, item)
##
##max_sub_arr([1,2,3,4,2,3,4],3)
##print("Total time taken: ",time.time()-start)

import unittest
import time
start = time.time()
def max_sub_array_of_size_k(arr,k):
  arr.sort()
  max_sum = sum(arr[-k:])
  return max_sum

class TestMaxSubArr(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3),10)
    def test_2(self):
        self.assertEqual(max_sub_array_of_size_k([2, 3, 4, 1, 5], 2),9)

if __name__ == '__main__':
    unittest.main(verbosity=3)
print("Total time taken: ",time.time()-start)
