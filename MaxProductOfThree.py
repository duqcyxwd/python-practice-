#!/usr/bin/env python
 
# For example, array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# contains the following example triplets:

# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# Your goal is to find the maximal product of any triplet.

# Write a function:

# int solution(int A[], int N);

# that, given a non-empty zero-indexed array A, returns the value of the maximal product of any triplet.

# For example, given array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.

# Assume that:

# N is an integer within the range [3..100,000];
# Complexity:

# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.


def solution1(A):
    # write your code in Python 2.7
    size = len(A)
    maxValue = 0;

    for x in xrange(0, size):
      for x1 in xrange(1, size):
        for x2 in xrange(2, size):
          if (x != x1 and x1 != x2 and x2 !=x):
            res = x * x1 * x2
            if res > maxValue:
              maxValue = res
    return maxValue

def solution(A):
    # write your code in Python 2.7
    size = len(A)
    maxValue = 0;
    i1 = 0
    i2 = size/2
    i3 = size - 1
    maxValue = A[i1] * A[i2] * A[i3]
    while true:
      maxValue = A[i1] * A[i2] * A[i3]

      pass
    return maxValue

def solution3(A):
    # write your code in Python 2.7
    size = len(A)
    sortedList = sorted(A)
    return sortedList[size-1] * sortedList[size-2] * sortedList[size-3]
print "hi"


A =  [-5, 5, -5, 4]
print A
print sorted(A)

print solution3(A)
A.sort()
print A
print max(1, 2, 3, 5)
