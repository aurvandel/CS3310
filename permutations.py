#Implement the permutation generating algorithm found in
#section 6.6 of our book. Do not use Python's built
#in permutation generator, and do not go to the web to
#find code. This is a programming class, so write your own
#code - closely following the algorithm presented in the book. Wrap the
#code in a main function so that your program prompts the user for any
#integer N between 1 and 9, and prints ALL permutations in lexicographic
#order for that N.

#procedure next permutation(a1a2 . . . an: permutation of
#    {1, 2, . . . , n} not equal to n n− 1 . . . 2 1)
#j := n − 1
#while aj > aj+1
#    j := j − 1
#{j is the largest subscript with aj < aj+1}
#k := n
#while aj > ak
#    k := k − 1
#{ak is the smallest integer greater than aj to the right of aj }
#interchange aj and ak
#r := n
#s := j + 1
#while r > s
#    interchange ar and as
#    r := r − 1
#    s := s + 1
#{this puts the tail end of the permutation after the jth position in increasing order}
#{a1a2 . . . an is now the next permutation}

#!/usr/bin/python3

import argparse


def main():
    #Get Command Line Arguments
    parser = argparse.ArgumentParser(description='Number 1-9')
    parser.add_argument('n', type=int, help='Number 1-9')
    args = parser.parse_args()
    
    # Check if number is between 1-9
    if args.n > 10 or args.n < 1:
        parser.error("Please enter a number between 1-9")
        
    # get the initial permutation value
    perms = initPermutations(args.n)    
    
    # make a list of the permutations as a list of tuples
    results = [tuple(perms)]
    
    while nextPermutation(perms):
        results.append(tuple(perms))

    for result in results:
        print(result)


#procedure next permutation(a1a2 . . . an: permutation of
#    {1, 2, . . . , n} not equal to n n− 1 . . . 2 1)
#j := n − 1
#while aj > aj+1
#    j := j − 1
#{j is the largest subscript with aj < aj+1}
#k := n
#while aj > ak
#    k := k − 1
#{ak is the smallest integer greater than aj to the right of aj }
#interchange aj and ak
#r := n
#s := j + 1
#while r > s
#    interchange ar and as
#    r := r − 1
#    s := s + 1
#{this puts the tail end of the permutation after the jth position in increasing order}
#{a1a2 . . . an is now the next permutation}
def nextPermutation(nums):
    size = len(nums)
    i = size - 1
    while i > 0 and nums[i - 1] > nums[i]:
        i -= 1
    j = i
    k = size - 1
    while j < k:
        nums[j], nums[k] = nums[k], nums[j]
        j += 1
        k -= 1
    if i == 0:
        return False
    else:
        j = i
        while nums[j] < nums[i - 1]:
            j += 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        return True
        
    
def initPermutations(num):
    # range object converted to list
    return list(range(1, num + 1))
        
    
if __name__ == "__main__":
    main()