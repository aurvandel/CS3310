#!/usr/bin/env python3
import random
import math

# TODO: Make main function accept command line arguments to make running this easier.
# TODO: Error handling for opening of files
# TODO: Error handling for characters that don't appear in the alphabet70
# TODO: Some test cases for the error handlers
# TODO: Test cases for the entire program

alphabet70 = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Write a class called RSA
class RSA:

    # Write a method called GenerateKeys that takes two very long text strings as input.
    def GenerateKeys(self, str1, str2):
        alphabet26 = "0123456789abcdefghijklmnopqrstuvwxyz"
        str1 = str1.replace(" ", "").lower()
        str2 = str2.replace(" ", "").lower()

        p = toBase10(alphabet26, str1, 26)
        q = toBase10(alphabet26, str2, 26)
        #mod by 10^200 to make them the right size. Ensure that they were longer than 10^200 before doing the mod, or print a Warning message.
        if p < 10**200:
            print("WARNING: number 1 is too small")
            digitCount(p)
        if q < 10**200:
            print("WARNING: number 2 is too small")
            digitCount(q)
        else:
            #Make them odd. Then start adding 2 until they are prime.
            p = p % 10**200
            if p % 2 == 0:
                p += 1
            q = q % 10**200
            if q % 2 == 0:
                q += 1
            while not isPrimeMiller(p):
                p += 2
            while not isPrimeMiller(q):
                q += 2

            #Now you have your two, 200 digit prime numbers, p and q.

            n = p * q
            r = (p - 1)*(q - 1)

            #Find e – a 398 digit number that is relatively prime with r.
            e = findRelativePrime(r)

            #Find d – the inverse of e mod r.
            d = inverse(e, r)

            #Save n and e to a file called public.txt (write them as text, with 1 return after each number)
            writeKeyToFile(n, "public.txt")
            writeKeyToFile(e, "public.txt")

            # Save n and d to a file called private.txt
            writeKeyToFile(n, "private.txt")
            writeKeyToFile(d, "private.txt")

    # Write a method called Encrypt that takes as parameters the name of an input text file and the name of an output text file.
    def Encrypt(self, inFile, outFile):
        plainText = openFile(inFile)

        # Treat the input file text as a base 70 integer, and convert it to base 10, using block sizes so as to not exceed integer n.
        blocks = []
        n, e = getKey("public.txt")
        while len(plainText) >= 200:
            newBlock = plainText[:200]
            newBlockNum = toBase10(alphabet70, newBlock, 70)
            blocks.append(newBlockNum)
            plainText = plainText[200:]
        # convert the last block
        lastBlock = toBase10(alphabet70, plainText, 70)
        blocks.append(lastBlock)

        # Encode each block using the rules of RSA.  (Read n and e from public.txt) C = M^e mod n.
        fullMsg = ''
        for block in blocks:
            msgNum = pow(block, e, n)
            msgTxt =toBaseN(alphabet70, msgNum, 70)
            msgTxt += '$'
            fullMsg += msgTxt

        writeEncryptedData(fullMsg, outFile)

    def Decrypt(self, inFile, outFile):
        n, d = getKey("private.txt")
        msgTxt = openFile(inFile)
        txtBlocks = msgTxt.split('$')
        msg = ''
        for item in txtBlocks:
            msgNum = toBase10(alphabet70, item, 70)
            decodedMsgNum = pow(msgNum, d, n)
            msg += toBaseN(alphabet70, decodedMsgNum, 70)
        writeEncryptedData(msg, outFile)


def writeEncryptedData(msg, filename):
    with open(filename, "wb") as file:
        file.write(msg.encode("utf-8"))

def getKey(fileName):
    with open(fileName, "rb") as file:
        lines = file.readlines()
    return int(lines[0]), int(lines[1])

def toBaseN(alphabet, n, base):
        result = ""
        if n == 0:
            return alphabet[0]
        while n != 0:
            result = alphabet[n % base] + result
            n = n // base
        if result == "":
            result = "0"
        return result

def openFile(inputfile):
    fin = open(inputfile, "rb")
    PlainTextBinary = fin.read()
    PlainText = PlainTextBinary.decode("utf-8")
    fin.close()
    return PlainText

def toBase10(alphabet, s, base):
    a = 0
    for c in s:
        value = alphabet.find(c)
        a *= base
        a += value
    return a

def egcd(a, b):
    lastR, r = abs(a), abs(b)
    x, lastX, y, lastY = 0, 1, 1, 0
    while r:
        lastR, (quotient, r) = r, divmod(lastR, r)
        x, lastX = lastX - quotient * x, x
        y, lastY = lastY - quotient * y, y
    return lastR, lastX * (-1 if a < 0 else 1), lastY * (-1 if b < 0 else 1)

def inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def computeGCD(x, y):
    while y:
        x, y = y, x % y
    return x

def findRelativePrime(n):
    # Should this be changed from 400 digits to 398 digits?
    nextN = n // 100
    while math.gcd(n, nextN) != 1:
        nextN += 1
    return nextN

def millersTest(n):
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

def isPrimeMiller(n):
    testTimes = 20
    for i in range(testTimes):
        ok = millersTest(n)
        if not ok:
            return False
    return True

def digitCount(number):
    count = 0
    while number > 0:
        number = number // 10
        count = count + 1

    print("\n Number of digits = %d" % count)

def writeKeyToFile(n, filename):
    with open(filename, 'a') as file:
        file.write(str(n))
        file.write('\n')


quote1 = "Wizards First Rule people are stupid Richard and Kahlan frowned even more People are stupid given proper " \
        "motivation almost anyone will believe almost anything Because people are stupid they will believe a lie " \
        "because they want to believe its true or because they are afraid it might be true"

quote2 = "A man will find a single coin in the mud and talk about it for days but when his inheritance comes and is" \
         " accounted one percent less than he expected then he will declare himself cheated"

def main():
    rsa = RSA()
    rsa.GenerateKeys(quote1, quote2)
    rsa.Encrypt("plainTextMsg.txt", "encryptedMsg.txt")
    rsa.Decrypt("encryptedMsg.txt", "decryptedMsg.txt")
    
    
main()

