# show the table for dynamic programming solution
#   for longeset increasing subsequence
#   input: 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 


import sys
import time

A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

# we use recursive formula:
# LISbigger(i, j) = {
#   0 if j > n
#   LISbigger(i, j+1) if A[j] <= A[i]
#   max(LISbigger(i, j+1), LISbigger(j, j+1) + 1) if A[j] > A[i]
# }
# since we using dynamic programming, 
# we implemt LISbigger(i, j) as a 2d array
# dp[i][j] = {
#   0 if j > n
#   dp[i][j+1] if A[j] <= A[i]
#   max(dp[i][j+1], dp[j][j+1] + 1) if A[j] > A[i]
# }

def printDPTable(A):
    n = len(A)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if A[j] <= A[i]:
                dp[i][j] = dp[i][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[j][j+1] + 1)
    print("DP Table:")
    # print the table in a nice format with column width 3
    # also print the input on top and on the left, separate from the table using underscores and pipes
    print("  ", end="")
    for i in range(n):
        print("{:3d}".format(A[i]), end="")
    print()
    print("_"*(3*n+2))
    for i in range(n):
        print("{:2d}|".format(A[i]), end="")
        for j in range(n):
            print("{:3d}".format(dp[i][j]), end="")
        print("|")
    print("_"*(3*n+2))

def main():
    printDPTable(A)

if __name__ == "__main__":
    main()