# Krista Koeplin
# Assignment TDD

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    """Test written to see if the folllowing requirements have been met.
       Range of 8-20 characters, one lower and one upper, one digit, onee
       symbol from the following list "~`!@#$%^&*()_+-= "."""

    def test1(self):
        """This test is to see if a empty stirng returns False as expected."""
        pwd = ""
        self.assertFalse(check_pwd(pwd))


if __name__ == '__main__':
    unittest.main()
