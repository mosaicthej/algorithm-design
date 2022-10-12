# use dynamic programming to solve the problem

# Problem: Building a stable disk pile
# Input: An array W[1...n] of n positive integers and an array C[1...n] of n positive integers. For each i from 1 to n, W[i] represents the weight of disk i and W[i]*C[i] represents the total weight that disk i can carry (In other words, putting more than W[i]*C[i] on top of disk i will break the disk).
# Output: The maximum number of disks that can be placed in a single pile (stacked one above the other) without breaking any disk. You do not need to find the sequence.
# Example: Input: W = [20, 40, 30] C = [2, 1, 1]. Output: 2 (because there is no way to pile 3 disks without breaking one of them) 
# Example: Input: W = [20, 40, 30] C = [2, 2, 2]. Output: 3 (because we can pile all 3 disks without breaking any of them)

# Example: Input: 
#   W = [1, 90, 20, 30, 40, 10]
#   C = [100, 1, 3, 1, 2, 9]
# Output: 4 (because we can pile all 4 disks without breaking any of them) 
from math import inf
from math import comb
from itertools import combinations
W = [1, 90, 50, 50, 40, 20, 30]
C = [100, 1, 2, 2, 1, 2, 1]
plate_capacity = [W[i]*C[i] for i in range(len(W))]

# first define pile_capacity, which is the total weight that a pile can carry
# when adding a plate:
# pile_capacity = min(pile_capacity - plate_weight, plate_capacity)

# recursive function to find the maximum number of disks that can be placed in a single pile
# assume we already have a pile with n-1 disks, 
# this pile can be A\A[i] for 1<=i<=n-1
# we need to find the maximum number of disks that can be placed in a single pile with A[i] added
# of all n different {A\A[i]} + A[i], we choose the one with the maximum number of disks, 
# and also give us a max pile_capacity



# a helper function to decide the optimal way to add the A[i] to the pile
def optimal_choice(L):
    # L is a list of tuples (number of disks, pile_capacity)
    # return the optimal number of disks and pile_capacity
    # pile_capacity only from the ones with the maximum number of disks (tied)
    max_num = 0
    max_pile_capacity = 0
    tie_ind = []
    for i in range(len(L)):
        if L[i][0] > max_num:
            max_num = L[i][0]
    
    for i in range(len(L)):
        if L[i][0] == max_num:
            tie_ind.append(i)
    
    for i in tie_ind:
        if L[i][1] > max_pile_capacity:
            max_pile_capacity = L[i][1]
    
    return (max_num, max_pile_capacity)

# helper function to add a disk to a pile (update the pile_capacity and number of disks)
def add_disk(pile_disk_num, pile_capacity, disk_weight, disk_capacity):
    # pile_disk_num is the number of disks in the pile
    # pile_capacity is the total weight that a pile can carry
    # disk_weight is the weight of the disk
    # disk_capacity is the total weight that the disk can carry
    # return the updated pile_disk_num and pile_capacity
    # if pile breaks, don't update pile_disk_num and pile_capacity
    temp = pile_capacity - disk_weight
    if disk_capacity < temp:
        temp = disk_capacity
    if temp >= 0:
        pile_disk_num += 1
        pile_capacity = temp
    return (pile_disk_num, pile_capacity)


# initialize A: a list of tuples (W[i], W[i]*C[i]) for 1<=i<=n
A = [(W[i], plate_capacity[i]) for i in range(len(W))]


# use dynamic programming to solve the problem
# store the results in a dictionary, key is the set of indices, value is the optimal number of disks and pile_capacity
# key is a set of indices, value is a tuple (number of disks, pile_capacity)
def diskPile(A):
    # A is a list of tuples (weight, capacity)
    # return the maximum number of disks that can be placed in a single pile
    # use dynamic programming to solve the problem
    # store the results in a dictionary, key is the set of indices, value is the optimal number of disks and pile_capacity
    # key is a set of indices, value is a tuple (number of disks, pile_capacity)
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return 1
    # initialize the dictionary
    D = dict()
    D[frozenset()] = (0, inf)
    # key is a set of indices, value is a tuple (number of disks, pile_capacity)
    key = frozenset()
    all_disks = frozenset(range(n)) # {0, 1, 2, ..., n}
    
    for i in range(n):
        for comb in combinations(range(n), i+1):
            key = frozenset(comb)
            # for each element in A\comb, add it to the pile
            outside = all_disks - key
            L = []
            for j in outside:
                L.append(add_disk(D[key][0], D[key][1], A[j][0], A[j][1]))
            D[key | frozenset([j])] = optimal_choice(L)
    return D[all_disks][0]

print(diskPile(A))
            



