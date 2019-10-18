import unittest
import RSA
import math

rsa = RSA.RSA()
alphabet70 = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


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


    def testToBaseN(self):
        self.assertEqual(RSA.toBaseN(alphabet70, 0, 70), '.')


    def test10to70AndBack(self):
        startingNumbers = [0, 596, 6732169763216889432, 4683559735441635]
        for num in startingNumbers:
            base70Num = RSA.toBaseN(alphabet70, num, 70)
            base10Conversion = RSA.toBase10(alphabet70, base70Num, 70)
            self.assertEqual(base10Conversion, num)


    def test70to10AndBack(self):
        startingStrings = ['alekslieshsle',
                           "Wizards First Rule people are stupid Richard and Kahlan",
                           "Wizards First Rule people are stupid Richard and Kahlan frowned even more People are stupid given proper " 
                           "motivation almost anyone will believe almost anything Because people are stupid they will believe a lie " 
                           "because they want to believe its true or because they are afraid it might be true"
                           ]
        for item in startingStrings:
            base10Num = RSA.toBase10(alphabet70, item, 70)
            base70Conversion = RSA.toBaseN(alphabet70, base10Num, 70)
            self.assertEqual(base70Conversion, item)


if __name__ == '__main__':
    unittest.main()
