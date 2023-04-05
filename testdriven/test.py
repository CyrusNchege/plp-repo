import unittest
from fizzbuzz import fizz_buzz


class FizzBuzzTest(unittest.TestCase):
    """
    Testing the fizzbuzz
    """

    def test_fizz(self):
        """
        Test return fizz when input is
        divisible by three
        """
        self.assertEqual(fizz_buzz(3), 'fizz')

    def test_buzz(self):
        """Test return buzz when input is
        divisible by five
        """
        self.assertEqual(fizz_buzz(5), 'buzz')
    
    def test_fizzbuzz(self):
        """Test return fizzbuzz when input is
        divisible by both 5 and 3
        """
        self.assertEqual(fizz_buzz(15), 'fizzbuzz')

    def test_number(self):
        """Test return number when not divisible
        by either 3 or 5
        """
        self.assertEqual(fizz_buzz(4), 4)

if __name__ == '__main__':
    unittest.main()