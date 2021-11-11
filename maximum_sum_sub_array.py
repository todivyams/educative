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

from itertools import combinations
import unittest
import time

start = time.time()
def max_sub_array_of_size_k(arr,k):
    arr_len = len(arr)
    if k> arr_len:
        print ("Error")
        return

    max_sum = arr[0]
    for ind in range(1,k):
        start = ind
        limit = start+k
        while limit <= arr_len:
            if sum(arr[start:limit]) > max_sum:
                max_sum = sum(arr[start:limit])
            start += k
            limit += k
    return max_sum

#max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3)   

class TestMaxSubArr(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3),9)
    def test_2(self):
        self.assertEqual(max_sub_array_of_size_k([2, 3, 4, 1, 5], 2),7)
print("Total time taken: ",time.time()-start)

##import unittest
##import time
##start = time.time()
##def max_sub_array_of_size_k(arr,k):
##  arr.sort()
##  max_sum = sum(arr[-k:])
##  return max_sum
##
##class TestMaxSubArr(unittest.TestCase):
##    def test_1(self):
##        self.assertEqual(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3),10)
##    def test_2(self):
##        self.assertEqual(max_sub_array_of_size_k([2, 3, 4, 1, 5], 2),9)

if __name__ == '__main__':
    unittest.main(verbosity=3)
print("Total time taken: ",time.time()-start)
