# Write a function:

# def solution(A)

# that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0) that does not occur in A.

# For example, given:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 6
#   A[3] = 4
#   A[4] = 1
#   A[5] = 2
# the function should return 5.

# Assume that:

# N is an integer within the range [1..100,000];
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.

def solution(A):
    # write your code in Python 2.7
    newList = sorted(A)
    
    for n in xrange(0, len(A) -1):
        if newList[n] + 1 != newList[n+1] and newList[n] != newList[n+1] and newList[n] + 1 > 0:
            return newList[n] + 1
    pass

print sorted([-1, 3, 2, 1])

print solution([-1, 3, 2, 1])
