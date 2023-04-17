# 17/04/2023
# https://www.youtube.com/watch?v=344uwF1z2Gg

import unittest

import primos


class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(primos.is_prime(4))
        self.assertTrue(primos.is_prime(2))
        self.assertTrue(primos.is_prime(3))
        self.assertFalse(primos.is_prime(8))
        self.assertFalse(primos.is_prime(10))
        self.assertTrue(primos.is_prime(7))
        self.assertEqual(primos.is_prime(-3),"Error. Número negativo.")


if __name__ == '__main__':
    unittest.main()