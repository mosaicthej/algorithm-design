'''
Write an efficient dynamic programming algorithm (to the best of your knowledge) for the following problem, briefly describe why it is a correct algorithm, provide pseudocode, and analyze the time complexity.  

Problem: Placing mobile guards along a highway
Input: An array A[1...n] of n distinct positive integers sorted in increasing order, and two integers p and q. Here A represents the positions along a horizontal line to be guarded. The numbers p and q represent the number of type P and type Q guards, respectively. Type P guards have a range of 1 unit in each direction (left and right). Type Q guards have a range of 3 units in each direction (left and right). You need to place these guards such that every location is within the range of at least one guard.
Task: Print 'Yes' if a placement to guard all locations is possible. Otherwise, print 'No'
Example: Input: A = [2, 4, 5, 7, 9, 11, 21], p = 1, q= 2. Output: Yes (Because you can place one type P guard at 3 and two type Q guards at 8 and 21.

Example: Input: A = [2, 4, 5, 7, 9, 11, 21], p = 1, q= 1. Output: No
'''

# idea:
# since the array is sorted, and we have to place guards at every location
# that means we have to cover the last location with a guard

# we put the guard at the optimal place, for last location
# if we use type p guard, which have a range of 1 unit in each direction
# then we place p at A[n] - 1
# then we cover from A[n] - 2 to A[n]

# if we use type q guard, which have a range of 3 units in each direction
# then we place q at A[n] - 3
# then we cover from A[n] - 6 to A[n]

# use a helper function to check how many locations are covered.
# k = covered locations by placing p or q
# then we reduce the problem to a smaller problem with n - k locations

# use dynamic programming, save the result in a 3d array with type boolean
# dp[i][j][k] = True if we can cover the first i locations with j type p guards and k type q guards

# things to check for each cell:
# for each dp[i][j][k]:
    # if i == 0:
    # dp[i][j][k] = True
    # since we have no locations to cover

    #　if i!= 0 and j == 0 and k == 0:
    # dp[i][j][k] = False
    # since we have no guards to place

    # if dp[i][j-1][k] == True:
    #   we already covered the first i locations with j-1 type p guards and k type q guards
    #   then for sure we can do that with one more type p guard (free p)

    # if dp[i][j][k-1] == True:
    #   we already covered the first i locations with j type p guards and k-1 type q guards
    #   then for sure we can do that with one more type q guard (free q)

    # else:
    #   we have to place a guard at the optimal place
    #   if we use type p guard, which have a range of 1 unit in each direction
    #   then we place p at A[i] - 1
    #   use the helper function to check how many locations are covered.
    #   k = covered locations by placing p or q
    #   then we reduce the problem to a smaller problem with i - k locations
        #  with j - 1 type p guards and k type q guards
        #  dp[i][j][k] == dp[i-k][j-1][k]
    
    #   if we use type q guard, which have a range of 3 units in each direction
    #   then we place q at A[i] - 3
    #   use the helper function to check how many locations are covered.
    #   k = covered locations by placing p or q
    #   then we reduce the problem to a smaller problem with i - k locations
        #  with j type p guards and k - 1 type q guards
        #  dp[i][j][k] == dp[i-k][j][k-1]
    

    # base case:
    # dp[0][0][0] = True
    # since we have no locations to cover, and no guards to place

# time complexity: O(n*p*q)
# space complexity: O(n*p*q)

def mobileGuard(Arr, p, q):
    # Arr is the array of locations
    # p is the number of type P guards
    # q is the number of type Q guards
    # return 'Yes' if a placement to guard all locations is possible. Otherwise, return 'No'

    n = len(Arr)
    dp = [[[False for _ in range(q+1)] for _ in range(p+1)] for _ in range(n+1)]
    dp[0][0][0] = True

    for i in range(n+1):
        for j in range(p+1):
            for k in range(q+1):
                if i == 0:
                    dp[i][j][k] = True
                elif i!= 0 and j == 0 and k == 0:
                    dp[i][j][k] = False
                elif dp[i][j-1][k] == True:
                    dp[i][j][k] = True
                elif dp[i][j][k-1] == True:
                    dp[i][j][k] = True
                else:
                    # use type p guard
                    c = checkNumber(Arr[:i], 1)
                    dp[i][j][k] = dp[i-c][j-1][k]
                    # use type q guard
                    c = checkNumber(Arr[:i], 3)
                    dp[i][j][k] = dp[i-c][j][k-1]

    if dp[n][p][q] == True:
        return 'Yes'
    else:
        return 'No'


# helper function to check how many locations are covered.
def checkNumber(Arr, guardRange):
    # Arr is the array of locations
    # guardRange is the range of the guard
    # return the number of locations covered by the guard
    # place the guard at the optimal place to cover the last location
    # count the number of locations covered by the guard

    last_loc = Arr[-1]
    guard_loc = last_loc - guardRange
    count = 0
    for i in range(len(Arr)):
        if Arr[i] >= guard_loc - guardRange and Arr[i] <= guard_loc + guardRange:
            count += 1
        else:
            continue
    return count


# test,
# in command line, print each step to see how the array is filled
# print the entire table for each step, use . to represent False, and * to represent True
# 0.1 second delay between each step
import time

A = [2, 4, 5, 7, 9, 11, 21]
p = 1
q = 2

def AnimatedMobileGuard(A, p, q):
    n = len(A)
    dp = [[[False for _ in range(q+1)] for _ in range(p+1)] for _ in range(n+1)]
    dp[0][0][0] = True

    for i in range(n+1):
        for j in range(p+1):
            for k in range(q+1):
                if i == 0:
                    dp[i][j][k] = True
                elif i!= 0 and j == 0 and k == 0:
                    dp[i][j][k] = False
                elif dp[i][j-1][k] == True:
                    dp[i][j][k] = True
                elif dp[i][j][k-1] == True:
                    dp[i][j][k] = True
                else:
                    # use type p guard
                    c = checkNumber(A[:i], 1)
                    dp[i][j][k] = dp[i-c][j-1][k]
                    # use type q guard
                    c = checkNumber(A[:i], 3)
                    dp[i][j][k] = dp[i-c][j][k-1]

                print('dp[{}][{}][{}] = {}'.format(i, j, k, dp[i][j][k]))
                time.sleep(0.1)
        print('''

''')

    if dp[n][p][q] == True:
        return 'Yes'
    else:
        return 'No'

AnimatedMobileGuard(A, p, q)