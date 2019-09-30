import random
import argparse


def millersTest(n):
    # Returns True if num is a prime number.
#    n = num - 1
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


def main():
    #Get Command Line Arguments
    parser = argparse.ArgumentParser(description='Enter a number')
    parser.add_argument('n', type=int, help='Any positive integer greater than 1')
    args = parser.parse_args()
    
    # Check if number is greater than 1
    if args.n <= 1:
        parser.error("Please enter a number greater than 1")
    
    # edge case to check for 2
    if args.n == 2:
        print("true")
    # bailout of number is even
    elif args.n % 2 == 0:
        print("false")
    elif isPrimeMiller(args.n):
        print("true")
    else:
        print("false")
   
   
if __name__ == "__main__":
    main()