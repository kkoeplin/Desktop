# Krista Koeplin
# Random Testing

from credit_card_validator import credit_card_validator
import random
import unittest


class TestCase(unittest.TestCase):
    def test_1Bug(self):
        for i in range(1000):
            # This is how many acceptable lengths of a credit card to test
            card_length = random.randint(10, 19)
            # Generates random numbers between o and 9
            card_number_string = ''.join(str(random.randint(0, 9)) for _ in range(card_length))
            credit_card_validator(card_number_string)


if __name__ == '__main__':
    unittest.main()
