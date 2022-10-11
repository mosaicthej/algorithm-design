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
# we can use a greedy approach to place the guards

