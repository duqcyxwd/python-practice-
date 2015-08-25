# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    resultCount = 0
    size = len(A)
    res = []
    for x in xrange(0,size):
        left = 0
        right = 0
        for z in xrange(0,x):
            left = left + A[z]

        for z in xrange(x + 1,size):
            right = right + A[z]

        print left
        print right
        if left == right:
            res.append(x)
            resultCount += 1
        print "\n"
    if resultCount != 0:
        return res
    else:
        return -1


if __name__ == '__main__':
    A = [-7, 1, 5, 2, -4, 3, 0]
    print solution(A)
    for x in xrange(1,1):
        print x


z = range(0, 10)
print z

print 3 / 2
