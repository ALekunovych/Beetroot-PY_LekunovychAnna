import unittest

#task 1
# test case from HW of lesson 13

def choose_func(nums: list, func1, func2):
    if all(numbers > 0 for numbers in nums):
        return func1(nums)
    return func2(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

class SquareTestCase(unittest.TestCase):

    def test_squares(self):
        self.assertEqual(square_nums(nums1), [1, 4, 9, 16, 25])

    def test_negatives(self):
        self.assertEqual(remove_negatives(nums2), [1, 3, 5])

    def test_choose(self):
        self.assertEqual(choose_func(nums1, square_nums, remove_negatives), [1, 4, 9, 16, 25])
        self.assertEqual(choose_func(nums2, square_nums, remove_negatives), [1, 3, 5])




if __name__ == '__main__':
    unittest.main()
