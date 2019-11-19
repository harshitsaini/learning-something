''' TOPICS - subsets for test case iterations '''

# python3 -m unittest unit_test_4 -v

import unittest


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest("hola"):
                self.assertEqual(i % 2, 0)
