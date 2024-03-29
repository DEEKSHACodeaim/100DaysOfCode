# 100DaysOfCode
This is the 100 days of code challenge that I took up decided to code everyday  and commit the progress everyday for 100 days 
# RULES:
I will code for at least an hour every day for the next 100 days.
Start Date:  
Jan 1st, 2023
# DAILY LOG:
## Day1-1/1/2023 ->Prefix Sum  
Solved 2 problems from leet code  
1.Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).  
  Return the running sum of nums.[leet code link](https://leetcode.com/problems/running-sum-of-1d-array/)  
  Time Complexity = O(n)  
  Space Complexity = O(n)  
  type: easy

2.Given an array of integers nums, calculate the pivot index of this array.  
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
[leet code link](https://leetcode.com/problems/find-pivot-index/)   
Time Complexity = O(n)    
Space Complexity = O(n)    
type: easy

## Day9-12/4/2023 ->Binary search based questions
Started 14 days of coding challenge on leetcode
1. [Binary Search](https://leetcode.com/problems/binary-search/description/?envType=study-plan&id=algorithm-i)  
   Time Complexity = O(log(n))  
   Space Complexity = O(1)  
   type= easy
  
2. [First Bad Version](https://leetcode.com/problems/first-bad-version/?envType=study-plan&id=algorithm-i)  
   Time Complexity = O(log(n))  
   Space Complexity = O(1)  
   type=easy
   
3. [Search Index position](https://leetcode.com/problems/search-insert-position/description/?envType=study-plan&id=algorithm-i)  
   Time Complexity = O(log(n))  
   Space Complexity = O(1)  
   type=easy
  
## Day10-13/4/2023 ->Two Pointers
Day 2 of the 14 day challenge
1. [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/?envType=study-plan&id)  
    approach- use two pointer if theere are negative number to square compare and add elements in sorted order to a new list that contains squared elements  
    Time Complexity = O(n)  
    Space Complexity = O(n)  
    type= easy  
2. [Rotate Array](https://leetcode.com/problems/rotate-array/)  
    approach - find k % len(list) that will be the actual number of elements coming to the front or rotated.Rotates all, rotate from 0 to k ( because that's the invertedpart from back), now finally rotate the the elements from the k+1 to len(list) as was original  
    Time Complexity = O(n)  
    Space Complexity = O(1)  
    type = medium  

## Day11-14/4/2023 ->Two Pointers
Day 3 of the 14 day challenge
1. [Move Zeroes](https://leetcode.com/problems/move-zeroes/)  
   Time Complexity = O(n)  
   Space Complexity = O(n)  
   type = easy  
2. [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  
   Time Complexity = O(n)  
   Space Complexity = O(n)  
   type= medium  

## Day12-15/4/2023 ->Two Pointers
Day 4 of the 14 daychallenge
1. [Reverse String](https://leetcode.com/problems/reverse-string/)  
   Time Complexity = O(n)  
   Space Complexity = O(1)  
   type= easy  
2. [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)  
   Time Complexity = O(n*s)  
   Space Complexity = O(n)  
   type= easy

## Day13-16/4/23 ->Two Pointers
Day 5 of 14 day challenge  
1. [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list)  
Time Complexity = O(n)  
Space Complexity = O(1)  
type = easy  

2. [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)  
Approach - two pointers at a distance of n -not simultanious updation at difference n  
Time Complexity = O(n)
Space Complexity = O(1)
type= medium

# Arrays

## Day 23 -26/7/23 
1. [Find the number of paths in a grid](https://leetcode.com/problems/unique-paths/description/)

   **brute force approach:**
   Resurssions-> left tree as solutions for downwards path and right sub tree as solution for rightwards paths
                                       base condition => 0 if out of bound and 1 if end found  
   Time Compelxity = O(2^n + 2^m)   
   Space Complexity = Depth of tree * each function call space\[Exponential]
   
   **better solution:**
   Dynamic programming: Store the solution in a matrix A\[m]\[n] and initial fill with -1
   Hint: Since the sub problem already discovered no need to find the solution again so store it ( there were repeated sub trees in the recurion tree-> preface)  
   Time complexity = O(n*m) \[ why? its bcs only those that are not computed in dp\[m]\[n]]  
   Space Complexity = O(n*m)
   type= medium

   **Optimal solution:**
   Combinations solution: n+m-2 C n-1 to be calculated as there are a toal of n-1+m-1 paths that can be choosen in n-1 ways or m-1 ways  
   Time complexity: O(n-1/m-1)  
   Space Complexity: O(1)   

2. [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/description/)

   **Brute force**
   O(n2) solution find all pairs from i to len(nums) for each element i and check for condition nums[i]>2*nums[j]

   **Optimal solution**
   count while merging in merge sort    
   Time Complexity = O(2n * log n)  
Type = Hard

## Day 24 -27/7/23 
1.[2 sum](https://leetcode.com/problems/two-sum/description/)  
Use hash table and store the complement along with its value as index number in the table  
Time Complexity = O(n)  
Space Complexity =O (n)   
type = Easy  

2.[4 sum](https://leetcode.com/problems/4sum/submissions/)
sort and have 2 pointer loop the other 2 for n iterations untill they cross each other check for i+j+k+l==target
Time Complexity = O(nlogn)[sort] + O(n^3)
Space Complexity = O(1) 
type= medium

## Day 25 -28/7/23
[Largest consecutive sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)
If there is an element lesser than that element present dont do any thing else untill there is an element greater than a current element in hashset increase the count
Time complexity = O(nlogn) (for each element in hashset search takes log n)
Space Complexity = O(n)

## Day 26 -29/7/23  
1. [Largest subarray with 0 sum](https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1)  

2. [Subarrays with XOR ‘K’](https://www.codingninjas.com/studio/problems/subarrays-with-xor-k_6826258?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0)  

## Day 27 -30/7/23
[Kadanes Algorithm]  



# Linked Lists  

## Day 28 -31/7/23
1. [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/)  
   Have 3 pointer initialize and iterate the loop until the next pointer is not void. For each iteration perform 2 operations:1) reverse next link 2) update the 3 pointer  
   Time = O(n), Space = O(n), type=easy  
2. [Middle Of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)  
   Use fast slow pointer    
   Time Complexity =O(n/2) Space =O(1) type= easy  
## Day 29 -1/8/23  
1.[Merge 2 sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)    
   Use the fact that the list pointer points to the entire list and can be assigned to the new list node   
   Time Complexity =O(n+m)  Space Complexity=O(n+m) type= easy    
2. [Remove nth node from the end of the list](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)  
   Use fast and slow pointer. Maintain the fast pointer n nodes ahead of the slow pointer. Iterate the list by moving fast and slow pointer by 1 until fast reaches the end, the slow pointer then points to n+1 node from the end. Use the slow pointer to remove the nth node.  
   Time Complexity= O(n) Space Complexity=O(1)  
   type = medium    
## Day 30 - 2/8/23  
1. [Add 2 number](https://leetcode.com/problems/add-two-numbers/)  
    Time Complexity =O(n+(m-n)) Space Complexity= O(n+(n-m))  type= medium  
2. [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)  
   Only that particular node is given so copy the next element to this node and remove the next node  
    Time Complexity = O(1)   Space=O(1)  type= medium  
