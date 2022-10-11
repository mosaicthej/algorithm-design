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

