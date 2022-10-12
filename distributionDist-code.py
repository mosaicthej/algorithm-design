# input:
# A[1...n], an array of integers

# k, an integer

# output array of integers with length k, B[1...k], B[i] in A
# for each element in A, A[i] can find a member in B, B[j] such that
# this B[j] is the closest element to A[i] in B, D[i] = |A[i] - B[j]|
# we want to find such B[1...k] that the sum of D[1...n] is minimized
# we can use dynamic programming to solve this problem 

# base case: k = n,
# B[1...n] = A[1...n]
# D[1...n] = 0
# sum(D[1...n]) = 0

# go from the base case, k=n, to k=1
# each time we reduce k by 1, we find one such B[i] to exclude from B[1...k+1]
# such that the sum of D[1...n] is minimized

# use dynamic programming, save the result in a 3d array with type integer
# dp[i][j][k] = minimum sum of D[1...n] if we exclude B[i] from B[1...k+1]

# need a helper function to calculate the sum of D[1...n] when given B[1...k] and A[1...n]
def sumD(B, A):
    # for each A[i], find the closest element in B
    # D[i] = |A[i] - B[j]|
    # return the sum of D[1...n]
    D = [0]*len(A)
    for i in range(len(A)):
        # find the closest element in B
        minD = abs(A[i] - B[0])
        for j in range(len(B)):
            if abs(A[i] - B[j]) < minD:
                minD = abs(A[i] - B[j])
        D[i] = minD
    return sum(D)







