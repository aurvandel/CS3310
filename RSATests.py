import unittest
import RSA
import math

rsa = RSA.RSA()
class MyTestCase(unittest.TestCase):

    def test26ToBase10SingleNumbers(self):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alphabet)):
            self.assertEqual(RSA.toBase10(alphabet[i], 26), i)


    def test26ToBase10BigNumbers(self):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
        tests = [
            ("aa44a1", 123456789),
            ("cd5emimlic", 67913549876132)
        ]
        for i in range(len(tests)):
            result = RSA.toBase10(alphabet, tests[i][0], 26)
            self.assertEqual(result, tests[i][1])


    def testComputeGCD(self):
        # some random gcd's to test
        tests = [
            (82, 12), (17, 3), (168, 82), (56893, 563)
        ]
        for test in tests:
            result = RSA.computeGCD(test[0], test[1])
            self.assertEqual(result[0], math.gcd(test[0], test[1]))


    def testFindRelativePrime(self):
        tests = [
            (8, 9), (14, 15), (20, 21)
        ]
        for test in tests:
            self.assertEqual(RSA.findRelativePrime(test[0]), test[1])


    def testInverse(self):
        tests = [
            (5, 11, 9), (3, 8, 3)
        ]
        for test in tests:
            self.assertEqual(RSA.inverse(test[0], test[1]), test[2])


if __name__ == '__main__':
    unittest.main()
