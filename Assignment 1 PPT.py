#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]


# In[28]:


def twosum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]

n = [2,7,11,15]
t = 9
print(twosum(n, t))


# In[ ]:


Q2. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5

Output: 2


# In[33]:


def return_index(arr, n, K):
    for i in range(n):
        if arr[i] == K:
            return i
        elif arr[i] > K:
            return i
    return n
arr = [1, 3, 5, 6]
n = len(arr)
K = 5
print(return_index(arr, n, K))


# In[ ]:


Q3.Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]

Output: true


# In[10]:


def checkDuplicatesWithinK(arr, num, k):
    for i in range(num):
        j = i + 1
        range_ = k
        while (range_ > 0 and j < num):
            if (arr[i] == arr[j]):
                return True
            j += 1
            range_ -= 1
    return False
arr = [1,2,3,1]
num = len(arr)
if (checkDuplicatesWithinK(arr, num, 3) == True):
    print("Yes")
else:
    print("No")


# In[ ]:


Q4. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


# In[5]:


def pushZerosToEnd(arr,n):
    count = 0 
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count+=1
    while count < n:
        arr[count] = 0
        count += 1
arr = [0,1,0,3,12]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)


# In[ ]:


Q5. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]


# In[19]:


def printTwoElements(arr, n):
    arr.sort()
    print("The repeating element is",end=" ")
    for i in range(0, n - 1):
        if(arr[i] == arr[i + 1]):
            print(arr[i])
            break

print("and the missing element is",end=" ")
for i in range(1, n + 1):
    if(i != arr[i - 1]):
        print(i)
        break

arr = [1,2,2,4]
n = len(arr)
printTwoElements(arr, n)


# In[ ]:




