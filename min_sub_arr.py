import unittest
sub_array = []
def smallest_subarray_with_given_sum(s, arr):
    if sum(arr) < s:
        print("No sub array")
        retrun 
    len_arr = len(arr)
    start = 0
    end = start + 1
    min_sub_len = len_arr
    while end <= len_arr:
        while end-start < min_sub_len:
            if sum(arr[start:end]) >= s:
                sub_array = arr[start:end]
                min_sub_len = end-start
                break
            else:
                end += 1
        start += 1
        end = start+1
    print(sub_array)
    return min_sub_len
            
  

class TestSmallSubArr(unittest.TestCase):
    def test_1(self):
        self.assertEqual(smallest_subarray_with_given_sum(7,[2,1,5,2,3,2]),2)
    def test_2(self):
        self.assertEqual(smallest_subarray_with_given_sum(7,[2,1,5,2,8]),1)
    def test_3(self):
        self.assertEqual(smallest_subarray_with_given_sum(7,[7,1,5,2,8]),1)
    def test_4(self):
        self.assertEqual(smallest_subarray_with_given_sum(8,[3,4,1,1,6]),3)
if __name__ == "__main__":
    unittest.main(verbosity=3)
