#!/usr/bin/env python3
import random

# Write a class called RSA
class RSA:
    def __init__(self):
        pass

    
    # Write a method called GenerateKeys that takes two very long text strings as input.
    def GenerateKeys(self, str1, str2):
        p = self.toBase10(str1, 26)
        q = self.toBase10(str2, 26)
        #mod by 10^200 to make them the right size. Ensure that they were longer than 10^200 before doing the mod, or print a Warning message.
        if num1 < 10**200:
            print("WARNING: number 1 is too small")
        if num2 < 10**200:
            print("WARNING: number 2 is too small")
        else:
            #Make them odd. Then start adding 2 until they are prime.
            p = p % 10**200
            if p % 2 == 0:
                p += 1
            q = q % 10**200
            if q % 2 == 0:
                q += 1
            while not self.isPrimeMiller(p):
                p += 2
            while not self.isPrimeMiller(q):
                q += 2
            #Now you have your two, 200 digit prime numbers, p and q.
            #Calculate n = p*q
            n = p * q
            #Calculate r = (p-1)*(q-1)
            r = (p - 1)*(q - 1)
            #Find e – a 398 digit number that is relatively prime with r.
            
            
    def toBase10(self, s, base):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
        a = 0
        for c in s:
            value = alphabet.find(c)
            a *= base
            a += value
        return a
    
    
    def millersTest(self, n):
        # Returns True if num is a prime number.
        t = n - 1
        s = 0
        while t % 2 == 0:
            # keep halving t while it is even (and use s
            # to count how many times we halve t)
            t = t // 2
            s += 1
        b = random.randrange(2, n)
        if pow(b, t, n) == 1:
            return True
        p = t
        for i in range(s):
            if pow(b, p, n) == n - 1:
                return True
            p *= 2
        return False


    def isPrimeMiller(self, n):
        testTimes = 20
        for i in range(testTimes):
            ok = self.millersTest(n)
            if not ok:
                return False
        return True
    
    
def main():
    rsa = RSA()
    num1, num2 = rsa.GenerateKeys('asdf', 'fdsa')
    print(num1, num2)
    # test to make sure the alphabet is mapped correctly
#    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
#    for c in alphabet:
#        print(c, "=", rsa.toBase10(c, 26))
        
    
    
main()
        