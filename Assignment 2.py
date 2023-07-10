#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q - Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn)
    such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.


# In[4]:


class Solution(object):
    def arrayPairSum(self, a):
        a = sorted(a)
        res = []
        for i in range(0, len(a), 2):
            res.append((a[i], a[i+1]))
        return sum([min(r) for r in res])
ob1 = Solution()
arr = [1,4,3,2]
print("The array is:",arr)
print("The maximum sum is:",ob1.arrayPairSum(arr))


# In[ ]:


Q - Given the integer array candyType of length n, return the maximum number of different types of candies she can eat 
    if she only eats n / 2 of them.


# In[16]:


def max_candies(candyType):
    max_num = len(set(candyType))
    num_to_eat = len(candyType) // 2
    return min(max_num, num_to_eat)
candyType=list(map(int, input("Enter a list of candys ").split()))
max_candies = max_candies(candyType)
print(max_candies)


# In[ ]:


Q - Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
    A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without
    changing the order of the remaining elements.


# In[ ]:


def subArray(arr, n):
    for i in range(0,n):
        for j in range(i,n):
            for k in range(i,j+1):
                print (arr[k],end=" ")
            print ("\n",end="")
arr =  [1,3,2,2,5,2,3,7]
n = len(arr)
print ("All Non-empty Subarrays") 
subArray(arr, n);


# In[ ]:


Q - You have a long flowerbed in which some of the plots are planted, and some are not.However, flowers cannot be planted
    in adjacent plots.Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty 
    and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent 
    flowers rule and false otherwise.


# In[ ]:


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, flower in enumerate(flowerbed):
            if flower == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
        n -= 1
        if n <= 0:
            return True
        return False


# In[ ]:


Q - Given an integer array nums, find three numbers whose product is maximum and return the maximum product.


# In[14]:


arr = [1,2,3]
product = 1
for num in arr:
    product = product * num
print(product)


# In[ ]:


Q - Given an array of integers nums which is sorted in ascending order, and an integer target,write a function to search
    target in nums. If target exists, then return its index. Otherwise,return -1.


# In[ ]:


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
 
        while l<=r:
            m = l + (r-l)//2
            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m
        return -1


# In[ ]:


Q - An array is monotonic if it is either monotone increasing or monotone decreasing.


# In[37]:


def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
      all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
A = [1,2,2,3]
print(isMonotonic(A))

